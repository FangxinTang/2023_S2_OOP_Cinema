"""Initialize the database"""
import uuid
import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import sql as sa_sql


engine = create_engine('postgresql://postgres:postgres@localhost/cinema', echo=True)
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )

    datetime_modified: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        server_default=sa_sql.func.now(),
        server_onupdate=sa_sql.func.now()
    )

    datetime_created: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        server_default=sa_sql.func.now()
    )

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