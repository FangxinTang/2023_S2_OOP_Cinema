"""Create Customer model"""
from .user import User


class Customer(User):
    __tablename__ = "customers"