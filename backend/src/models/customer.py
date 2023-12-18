"""Database ORM models"""
from ..users.models import User


class Customer(User):
    """class Customer"""
    __tablename__ = "customer"

