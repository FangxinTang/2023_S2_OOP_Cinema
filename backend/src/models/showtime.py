"""Create ShowTime model"""
from datetime import date, time
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel

class ShowTime(BaseModel):
    __tablename__ = "showtimes"

    show_date: Mapped[date] = mapped_column(
        unique=False,
        default="2000-10-10"
    )

    start_time: Mapped[time] = mapped_column(
        nullable=True,
        default="10:30:00"
    )

    end_time: Mapped[time] = mapped_column(
        nullable=True,
        default="12:30:00"
    )

