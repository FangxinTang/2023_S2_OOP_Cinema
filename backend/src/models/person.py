"""Database ORM models"""
from typing_extensions import Annotated
from sqlalchemy import orm
from ..db_init import Base



required_field = Annotated[str, orm.mapped_column(nullable=False, unique=True)]

class Person(Base):
    """Abstract class Person"""
    __abstract__ = True

    name: orm.Mapped[str] = orm.mapped_column(nullable=False)
    address: orm.Mapped[str] = orm.mapped_column(nullable=True)
    email: orm.Mapped[required_field]
    phone: orm.Mapped[required_field]


# ==== DUMMY DATA ==== #

# DUMMY_DATA = [
#     (
#         Person,
#         {
#             "name": "Sam Wang",
#             "address": "1000 Alison Street, Mangere, Auckland",
#             "email": "sam@example.com",
#             "phone": "12345678",
#         },
#     )
# ]


# ==== REGISTER ==== #

# MODELS_REGISTER = [Person]
