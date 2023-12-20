"""Create ShowTime model"""
from datetime import date, time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel

class ShowTime(BaseModel):
    __tablename__ = "showtimes"

    show_date: Mapped[date] = mapped_column(nullable=True)
    start_time: Mapped[time] = mapped_column(nullable=True)
    end_time: Mapped[time] = mapped_column(nullable=True)

    admin_id = mapped_column(ForeignKey("admin.id"))
    admin = relationship("Admin", back_populates="showtimes")

    movie_id = mapped_column(ForeignKey('movie.id'))
    movie = relationship('Movie', back_populates="movies")

    bookings = relationship('Booking', back_populates='showtime')

    hall_id =relationship(ForeignKey('hall.id'))
    hall = relationship('Hall', back_populates='showtimes')

    
