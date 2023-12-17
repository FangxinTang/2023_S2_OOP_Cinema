"""Database ORM models"""
from sqlalchemy import orm
from ..users import models as user_models


class FrontStaff(user_models):
    """class FrontStaff"""
    __tablename__ = "frontstaff"



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

MODELS_REGISTER = [FrontStaff]
