"""Database ORM models"""
from sqlalchemy import orm
from ..users import models as user_models


class Admin(user_models):
    """class Admin"""
    __tablename__ = "admin"



# ==== DUMMY DATA ==== #

# DUMMY_DATA = [
#     (
#         User,
#         {
#             "username": "sam_wang",
#             "password": "secretpass"
#         },
#     )
# ]


# ==== REGISTER ==== #

MODELS_REGISTER = [Admin]
