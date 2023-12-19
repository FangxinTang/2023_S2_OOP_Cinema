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

    showtime_id = mapped_column(ForeignKey("showtimes.id"))
    showtime = relationship("Admin", back_populates="showtimes")
