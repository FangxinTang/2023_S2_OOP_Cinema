"""Database ORM models"""
from sqlalchemy import orm
from .. import models as global_models ##### import error



required_field = orm.mapped_column(nullable=False, unique=True)


class Person(global_models.Base):
    """Abstract class Person"""
    __tablename__ = "person"

    name: orm.Mapped[str] = orm.mapped_column(nullable=False)
    address: orm.Mapped[str] = orm.mapped_column(nullable=True)
    email: orm.Mapped[str] = required_field
    phone: orm.Mapped[str] = required_field


# ==== DUMMY DATA ==== #

DUMMY_DATA = [
    (
        Person,
        {
            "name": "Sam Wang",
            "address": "1000 Alison Street, Mangere, Auckland",
            "email": "sam@example.com",
            "phone": "12345678",
        },
    )
]


# ==== REGISTER ==== #

# MODELS_REGISTER = [Person]
