"""Person(Abstract) models"""
from dataclasses import dataclass
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, composite
from database.db_init import BaseModel # import from an external package


required_unique_string = Annotated[
    str,
    mapped_column(
        String(128),
        nullable=False,
        unique=True
        )
    ]


@dataclass
class AddressDataClass:
    line_1: str
    line_2: str
    country: str


class Person(BaseModel):
    __abstract__ = True

    name: Mapped[str] = mapped_column(nullable=False)
    
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

    email: Mapped[required_unique_string]
    phone: Mapped[required_unique_string]
