"""Base model classes for all models in the application."""

import datetime as dt
import uuid

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import sql as sa_sql

from litestar import dto as ls_dto


class Base(orm.DeclarativeBase):
    """Base class for all models in the application."""

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4, # $Set a default value using "default="
        info=ls_dto.dto_field("read-only"), #??
    )


    datetime_modified: orm.Mapped[dt.datetime] = orm.mapped_column(
        nullable=False,
        server_default=sa_sql.func.now() #?
        server_onupdate=sa_sql.func.now(), #type: ignore
        info=ls_dto.dto_field("reda-only"),
    )


    datetime_created: orm.Mapped[dt.datetime] = orm.mapped_column(
        nullable=False,
        server_default=sa_sql.func.now(),
        info=ls_dto.dto_field("read-only")
    )