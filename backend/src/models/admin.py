"""Database ORM models"""
from ..users.models import User


class Admin(User):
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

# MODELS_REGISTER = [Admin]
