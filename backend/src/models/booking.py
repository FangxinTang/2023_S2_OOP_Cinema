"""Create ShowTime model"""
import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel


class ShowTime(BaseModel):
    __tablename__ = "showtimes"

    show_date: Mapped[dt.datetime] = mapped_column(
        unique=False,
        default=dt.datetime(2000, 10, 10)
    )

    start_time: Mapped[dt.datetime] = mapped_column(
        nullable=True,
        default=dt.datetime(10, 30)
    )

    end_time: Mapped[dt.datetime] = mapped_column(
        nullable=True,
        default=dt.datetime(12, 30)
    )

