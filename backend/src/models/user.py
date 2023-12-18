"""User(Abstract) model"""
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .person import Person # import from the same package


required_unique_string = Annotated[str, mapped_column(String(128), nullable=False, unique=True)]

class User(Person):
    __abstract__ = True

    username: Mapped[required_unique_string] 
    password: Mapped[required_unique_string]
