"""Create Staff model"""
from .user import User


class Staff(User):
    __tablename__ = "staff"