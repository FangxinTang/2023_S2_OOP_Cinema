"""Database management functions.
In charge of creating the schema, creating the tables,
and populating the tables with demo data."""

import logging
import uuid
from typing import Any, Type

import sqlalchemy as sa
from litestar import datastructures
from litestar.contrib.sqlalchemy import plugins as ls_sqlalchemy
from sqlalchemy import engine, orm
from sqlalchemy import schema as sa_schema
from sqlalchemy import sql as sa_sql

from .. import config as global_config
from .. import models as global_models
from ..database import core, utils


def check_existence_of_demo_item(
    session: orm.Session, table
) -> None | Type[global_models.Base]:
    """Checks if a demo item exists in the database.

    If it does, returns the model class for the item.
    If it doesn't, returns None.
    """
    return (
        session.execute(
            sa.select(table).where(table.id == "00000000-0000-0000-0000-000000000000")
        )
        .scalars()
        .first()
    )


def populate_demo_data(session: orm.Session):
    """Populates the database with data."""

    from ..packages import models as package_models
    from ..providers import models as provider_models
    from ..scratch_route import models as scratch_models
    from ..services import models as service_models
    from ..staff import models as staff_models

    # Combine DUMMY_DATA constants into one list.
    DUMMY_DATA: list[tuple[Type[global_models.Base], dict[str, Any]]] = [
        *scratch_models.DUMMY_DATA,
        *provider_models.DUMMY_DATA,
        *package_models.DUMMY_DATA,
        *service_models.DUMMY_DATA,
        *staff_models.DUMMY_DATA,
    ]  # pylint: disable=invalid-name

    objects = []

    for model, data in DUMMY_DATA:
        existing_item = check_existence_of_demo_item(session, model)
        demo_item = (
            existing_item
            if existing_item is not None
            else model(
                **data,
                id=uuid.UUID("00000000-0000-0000-0000-000000000000"),
            )
        )
        objects.append(demo_item)

    return objects


def init_database(config: ls_sqlalchemy.SQLAlchemyAsyncConfig):
    """Initializes the database. Creates the schema if it doesn't exist.
    Creates the tables if they don't exist."""
    logger = logging.getLogger()

    database_uri = config.connection_string
    schema_name = "public"

    # Create as synchronous engine
    url = sa.engine.url.make_url(database_uri).set(drivername="postgresql+psycopg2")

    if not utils.database_exists(url):
        logger.critical("Database doesn't exist. Creating...")
        utils.create_database(url)

    db_engine: engine.Engine = engine.create_engine(url)

    if not db_engine.dialect.has_schema(db_engine.connect(), schema_name):
        logger.critical("Schema %s doesn't exist. Creating..." % schema_name)
        with db_engine.connect() as connection:
            connection.execute(sa_schema.CreateSchema(schema_name))
            connection.commit()

    db_engine.connect().execute(
        sa.text("GRANT ALL ON SCHEMA public TO {user}".format(user=url.username))
    )

    global_config.MODELS_METADATA.create_all(db_engine)

    # pylint: disable=protected-access

    with orm.Session(db_engine) as conn:
        # Check if the tables are empty. If so, populate them with demo data.

        for table in global_config.MODELS_REGISTER[1:]:
            logger.critical("Checking if %s table is empty..." % table.__tablename__)
            query = sa.select(table).limit(1)
            result = conn.execute(query).fetchall()
            if not result:
                logger.critical(
                    "No data in %s table. Populating with demo data..."
                    % table.__tablename__
                )

                objects = populate_demo_data(conn)
                conn.add_all(objects)
                conn.commit()
                break
