"""Database ORM models"""
from sqlalchemy.orm import relationship
from .user import User


class Admin(User):
    __tablename__ = "admin"



