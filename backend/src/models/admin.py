"""Create Admin model"""
from .user import User


class Admin(User):
    __tablename__ = "admin"