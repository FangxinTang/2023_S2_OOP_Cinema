"""Create Movie model"""
from datetime import datetime as dt
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel

class Movie(BaseModel):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        unique=True
    )

    description: Mapped[str] = mapped_column(
        String(150),
        nullable=True
    )

    duration_mins: Mapped[int] = mapped_column(
        nullable=True,
        default=120
    )

    language: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
        default="English"
    )

    release_date: Mapped[dt] = mapped_column(
        nullable=True
    )

    country: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    genre: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            'duration_mins > 30 AND duration_mins < 250',
            name='duration_mins_range'
        ),
    )

