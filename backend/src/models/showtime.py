"""Create ShowTime model"""
import uuid
from typing import List
from datetime import date, time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel
from .admin import Admin
from .movie import Movie
from .hall import Hall
from .booking import Booking


class ShowTime(BaseModel):
    __tablename__ = "showtimes"

    show_date: Mapped[date] = mapped_column(nullable=True)
    start_time: Mapped[time] = mapped_column(nullable=True)
    end_time: Mapped[time] = mapped_column(nullable=True)

    admin_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("admins.id"))
    admin: Mapped['Admin'] = relationship(back_populates="showtimes")

    movie_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('movies.id'))
    movie: Mapped['Movie'] = relationship(back_populates="movies")

    bookings: Mapped[List['Booking']] = relationship(back_populates='showtime')

    hall_id: Mapped[uuid.UUID] =mapped_column(ForeignKey('halls.id'))
    hall: Mapped['Hall'] = relationship(back_populates='showtimes')

    
