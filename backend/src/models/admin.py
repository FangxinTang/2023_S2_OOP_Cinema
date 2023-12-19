"""Create Admin model"""
from sqlalchemy.orm import relationship
from .user import User


class Admin(User):
    __tablename__ = "admin"

    showtimes = relationship("ShowTime", back_populates="admin")
    movies = relationship("Movie", back_populates="admin")
