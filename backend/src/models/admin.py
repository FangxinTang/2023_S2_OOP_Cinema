"""Create Admin model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from .user import User
from .showtime import ShowTime
from .movie import Movie


class Admin(User):
    __tablename__ = "admins"

    showtimes: Mapped[List['ShowTime']] = relationship(back_populates="admin")
    movies: Mapped[List['Movie']] = relationship(back_populates="admin")
