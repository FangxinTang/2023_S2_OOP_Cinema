"""Database ORM models"""
from ..users.models import User


class FrontStaff(User):
    """class FrontStaff"""
    __tablename__ = "frontstaff"



# ==== DUMMY DATA ==== #
##..##

# ==== REGISTER ==== #

# MODELS_REGISTER = [FrontStaff]
