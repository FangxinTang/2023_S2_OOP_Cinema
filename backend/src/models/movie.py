"""Movie Model"""
import uuid
import datetime as dt
from typing import List
from sqlalchemy import String, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_model import BaseModel



class Movie(BaseModel):
    """Representing a movie in the database."""
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

    release_date: Mapped[dt.date] = mapped_column(
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

    # many-to-one
    admin_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('admins.id'))
    admin: Mapped['Admin'] = relationship(back_populates='movies')

    # one-to-many
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates="movie")

    def __repr__(self):
        admin_name = self.admin.name if self.admin else None
        showtimes_count = len(self.showtimes) if self.showtimes else 0
        return(f"<Moive(\n" 
               f"  title='{self.title}'\n"
               f"  duration_min={self.duration_mins},\n"
               f"  language='{self.language}',\n"
               f"  release_date={self.release_date},\n"
               f"  country='{self.country},\n "
               f"  genre='{self.genre}',\n"
               f"  admin= {admin_name},\n"
               f"  showtimes_count={showtimes_count}>")