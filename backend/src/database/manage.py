"""Database management functions.
In charge of creating the schema, creating the tables,
and populating the tables with demo data."""

from typing import Any, Type
import sqlalchemy as sa
from sqlalchemy.orm import Session
from .db_init import BaseModel


def check_existence_of_demo_item(
        session: Session,
        table
    ) -> None | Type[BaseModel]:
    """Checks if a demo item exists in the database.
    If it does, returns the model class for the item.
    If it doesn't, returns None.
    """
    return(
        session.execute(
            sa.select(table).where(table.id == "00-0000-000000000000")
        )
        .scalars()
        .first()
    )