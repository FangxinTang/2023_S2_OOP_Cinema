"""Create BaseModel with attributes"""
import uuid
import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from models.base_for_all import Base


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )

    datetime_modified: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.now()
    )

    datetime_created: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        server_default=func.now()
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