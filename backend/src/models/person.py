"""Person Abstract"""
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.base_model import BaseModel

PersonRequiredUniqueString = Annotated[str,
    mapped_column(String(128), nullable=False, unique=True)]

class Person(BaseModel):
    """Abstract base class representing a person."""

    __abstract__ = True

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[PersonRequiredUniqueString]
    phone: Mapped[PersonRequiredUniqueString]

    # Define address components as individual columns
    address_line_1: Mapped[str] = mapped_column(String(255))
    address_line_2: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(128))

    def __repr__(self):
        """Return a string representation of the Person object."""
        address = f"{self.address_line_1}, {self.address_line_2}, {self.country}"
        return f"<Person(\n name={self.name}, email={self.email}, phone={self.phone}, address={address}')>"


