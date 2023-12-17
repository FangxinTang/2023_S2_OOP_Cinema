import copy

import sqlalchemy as sa
from sqlalchemy.orm import exc as orm_exc
from sqlalchemy.orm import session as sa_session


def database_exists(database_uri: str | sa.URL) -> bool:
    try:
        engine = sa.create_engine(database_uri)
        engine.connect()
        return True
    except Exception as e:  # TODO - narrow exception
        print(e)
        return False


def _set_url_database(url: sa.URL, database):
    """Set the database of an engine URL.

    :param url: A SQLAlchemy engine URL.
    :param database: New database to set.

    """
    if hasattr(url, "_replace"):
        # Cannot use URL.set() as database may need to be set to None.
        ret = url._replace(database=database)
    else:  # SQLAlchemy <1.4
        url = copy.copy(url)
        url.database = database
        ret = url
    assert ret.database == database, ret
    return ret


def get_bind(obj):
    """
    Return the bind for given SQLAlchemy Engine / Connection / declarative
    model object.

    :param obj: SQLAlchemy Engine / Connection / declarative model object

    ::

        from sqlalchemy_utils import get_bind


        get_bind(session)  # Connection object

        get_bind(user)

    """
    if hasattr(obj, "bind"):
        conn = obj.bind
    else:
        try:
            conn = sa_session.object_session(obj).bind
        except orm_exc.UnmappedInstanceError:
            conn = obj

    if not hasattr(conn, "execute"):
        raise TypeError(
            "This method accepts only Session, Engine, Connection and "
            "declarative model objects."
        )
    return conn


def quote(mixed, ident):
    """
    Conditionally quote an identifier.
    ::


        from sqlalchemy_utils import quote


        engine = create_engine('sqlite:///:memory:')

        quote(engine, 'order')
        # '"order"'

        quote(engine, 'some_other_identifier')
        # 'some_other_identifier'


    :param mixed: SQLAlchemy Session / Connection / Engine / Dialect object.
    :param ident: identifier to conditionally quote
    """
    if isinstance(mixed, sa.Dialect):
        dialect = mixed
    else:
        dialect = get_bind(mixed).dialect
    return dialect.preparer(dialect).quote(ident)


def create_database(url: str | sa.URL, encoding="utf8", template=None):
    """Issue the appropriate CREATE DATABASE statement.

    :param url: A SQLAlchemy engine URL.
    :param encoding: The encoding to create the database as.
    :param template:
        The name of the template from which to create the new database. At the
        moment only supported by PostgreSQL driver.

    To create a database, you can pass a simple URL that would have
    been passed to ``create_engine``. ::

        create_database('postgresql://postgres@localhost/name')

    You may also pass the url from an existing engine. ::

        create_database(engine.url)

    Has full support for mysql, postgres, and sqlite. In theory,
    other database engines should be supported.
    """

    url = sa.make_url(url)
    database = url.database
    dialect_name = url.get_dialect().name
    dialect_driver = url.get_dialect().driver

    if dialect_name == "postgresql":
        url = _set_url_database(url, database="postgres")
    elif dialect_name == "mssql":
        url = _set_url_database(url, database="master")
    elif dialect_name == "cockroachdb":
        url = _set_url_database(url, database="defaultdb")
    elif not dialect_name == "sqlite":
        url = _set_url_database(url, database=None)

    if (dialect_name == "mssql" and dialect_driver in {"pymssql", "pyodbc"}) or (
        dialect_name == "postgresql"
        and dialect_driver
        in {"asyncpg", "pg8000", "psycopg", "psycopg2", "psycopg2cffi"}
    ):
        engine = sa.create_engine(url, isolation_level="AUTOCOMMIT")
    else:
        engine = sa.create_engine(url)

    if dialect_name == "postgresql":
        if not template:
            template = "template1"

        with engine.begin() as conn:
            text = "CREATE DATABASE {} ENCODING '{}' TEMPLATE {}".format(
                quote(conn, database), encoding, quote(conn, template)
            )
            conn.execute(sa.text(text))

    elif dialect_name == "mysql":
        with engine.begin() as conn:
            text = "CREATE DATABASE {} CHARACTER SET = '{}'".format(
                quote(conn, database), encoding
            )
            conn.execute(sa.text(text))

    elif dialect_name == "sqlite" and database != ":memory:":
        if database:
            with engine.begin() as conn:
                conn.execute(sa.text("CREATE TABLE DB(id int)"))
                conn.execute(sa.text("DROP TABLE DB"))

    else:
        with engine.begin() as conn:
            text = f"CREATE DATABASE {quote(conn, database)}"
            conn.execute(sa.text(text))

    engine.dispose()
