"""Person(Abstract) models"""
from dataclasses import dataclass
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, composite
from database.db_init import BaseModel  # import from an external package


RequiredUniqueString = Annotated[
    str,
    mapped_column(
        String(128),
        nullable=False,
        unique=True
    )
]


@dataclass
class AddressDataClass:
    """Data class representing a postal address"""
    line_1: str
    line_2: str
    country: str


class Person(BaseModel):
    """Abstract base class representing a person."""

    __abstract__ = True

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[RequiredUniqueString]
    phone: Mapped[RequiredUniqueString]

    # Define address components as individual columns
    address_line_1: Mapped[str] = mapped_column()
    address_line_2: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()

    # Use composite to create an Address object
    address: Mapped[AddressDataClass] = composite(
        "address_line_1",
        "address_line_2",
        "country"
    )

    def __repr__(self):
        """Return a string representation of the Person object."""
        address = f"{self.address_line_1}, {self.address_line_2}, {self.country}"
        return f"<Person(\n name={self.name},\n email={self.email},\n phone={self.phone},\n address='{address}'\n)>"
