"""Database ORM models"""
from sqlalchemy import orm
from ..users import models as user_models


class FrontStaff(user_models.User):
    """class FrontStaff"""
    __tablename__ = "frontstaff"



# ==== DUMMY DATA ==== #
##..##

# ==== REGISTER ==== #

# MODELS_REGISTER = [FrontStaff]
