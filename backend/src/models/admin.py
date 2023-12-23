"""Create Admin model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from .user import User
# from .showtime import ShowTime
# from .movie import Movie


class Admin(User):
    __tablename__ = "admins"

    # one-to-many 
    movies: Mapped[List['Movie']] = relationship(back_populates="admin")
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates="admin")


    def __repr__(self):
        user_repr = super().__repr__()
        movies_count = len(self.movies) if self.movies else 0
        showtimes_count = len(self.showtimes) if self.showtimes else 0

        return f"<Admin(\n {user_repr},\n movies_count={movies_count},\n showtimes_count={showtimes_count})>"
