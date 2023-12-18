"""Database ORM models"""
from typing_extensions import Annotated
# import sys
# import pathlib as pl
# sys.path.insert(0, str(pl.Path(__file__).resolve().parent.parent))
from ..models import Person
from sqlalchemy import orm

required_field = Annotated[str, orm.mapped_column(nullable=False, unique=True)]

class User(Person):
    __tablename__ = "users"

    username: orm.Mapped[required_field] 
    password: orm.Mapped[required_field]


# # ==== DUMMY DATA ==== #

# DUMMY_DATA = [
#     (
#         User,
#         {
#             "username": "sam_wang",
#             "password": "secretpass"
#         },
#     )
# ]


# # ==== REGISTER ==== #

# MODELS_REGISTER = [User]
