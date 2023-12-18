"""Initialize the database"""

import uuid
import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy import orm
from sqlalchemy import sql as sa_sql

engine = create_engine('postgresql://postgres:postgres@localhost/cinema', echo=True)

class Base(orm.declarative_base):
    """Base class for all models in the application."""

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )

    datetime_modified: orm.Mapped[dt.datetime] = orm.mapped_column(
        nullable=False,
        server_default=sa_sql.func.now(),
        server_onupdate=sa_sql.func.now()
    )


    datetime_created: orm.Mapped[dt.datetime] = orm.mapped_column(
        nullable=False,
        server_default=sa_sql.func.now()
    )

## use scenario?
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, key):
        return hasattr(self, key)

    def keys(self):
        items = self.__mapper__.attrs.keys()
        return items

    def get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)
        return default

    def items(self):
        return [(key, getattr(self, key)) for key in self.keys()]

    def values(self):
        return [getattr(self, key) for key in self.keys()]

    def __iter__(self):
        return iter(self.keys())

Base.metadata.create_all(engine)

Session = orm.sessionmaker(bind=engine)