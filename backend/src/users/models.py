"""Database ORM models"""
from sqlalchemy import orm
from ..persons import models as person_models


required_field = orm.mapped_column(nullable=False, unique=True)

class User(person_models):
    """Abstract class User"""
    __tablename__ = "users"

    username: orm.Mapped[str] = required_field
    password: orm.Mapped[str] = orm.mapped_column(nullable=False)


# ==== DUMMY DATA ==== #

DUMMY_DATA = [
    (
        User,
        {
            "username": "sam_wang",
            "password": "secretpass"
        },
    )
]


# ==== REGISTER ==== #

MODELS_REGISTER = [User]
