"""ShowTime Model"""
import uuid
import datetime as dt
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_model import BaseModel



class ShowTime(BaseModel):
    __tablename__ = "showtimes"

    show_date: Mapped[dt.date] = mapped_column(nullable=True)
    start_time: Mapped[dt.time] = mapped_column(nullable=True)
    end_time: Mapped[dt.time] = mapped_column(nullable=True)

    # Relationship with Admin - Many to one
    admin_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("admins.id"))
    admin: Mapped['Admin'] = relationship(back_populates="showtimes")

    # Relationship with Movie - Many to one
    movie_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('movies.id'))
    movie: Mapped['Movie'] = relationship(back_populates="showtimes")

    # Relationship with Hall - Many to one
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('halls.id'))
    hall: Mapped['Hall'] = relationship(back_populates='showtimes')

    # Relationship with Booking - One to many
    bookings: Mapped[List['Booking']] = relationship(back_populates='showtime')

    def __repr__(self):
        admin_name = self.admin.name if self.admin else 'No admin'
        movie_title = self.movie.title if self.movie else 'No movie'
        hall_name = self.hall.name if self.hall else 'No hall'
        bookings_count = len(self.bookings) if self.bookings else 0
        
        return (f"<ShowTime(\n"
            f"  show_date={self.show_date},\n"
            f"  start_time={self.start_time},\n"
            f"  end_date={self.end_time},\n"
            f"  admin={admin_name},\n"
            f"  movie_title={movie_title},\n"
            f"  hall={hall_name},\n"
            f"  bookings_count={bookings_count}\n)>")