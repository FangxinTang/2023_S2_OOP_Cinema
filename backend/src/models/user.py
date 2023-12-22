"""User(Abstract) model"""
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .person import Person


RequiredUniqueString = Annotated[
    str,
    mapped_column(
        String(128),
        nullable=False,
        unique=True
        )
    ]

class User(Person):
    """Abstract base class representing a user with unique username and password."""

    __abstract__ = True

    username: Mapped[RequiredUniqueString]
    password: Mapped[RequiredUniqueString]


    def __repr__(self):
        person_repr = super().__repr__()
        return f"<User(\n {person_repr},\n username={self.username}\n)>"
