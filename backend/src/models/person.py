"""Person(Abstract) models"""
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel


required_unique_string = Annotated[str, mapped_column(String(128), nullable=False, unique=True)]

class Person(BaseModel):
    __abstract__ = True

    name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[required_unique_string]
    phone: Mapped[required_unique_string]
