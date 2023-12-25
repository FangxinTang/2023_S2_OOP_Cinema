"""Hall Model"""
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_model import BaseModel


class Hall(BaseModel):
    __tablename__ = "halls"

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)

    # Relationship with ShowTime: 1 to many
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates='hall')

    # Relationship with Seat: 1 to Many
    seats: Mapped[List['Seat']] = relationship(back_populates='hall')

    def __repr__(self):
        showtimes_count = len(self.showtimes) if self.showtimes else 0
        seats_count = len(self.seats) if self.seats else 0
        return (
            f"<Hall(\n name={self.name}, total_seats={self.total_seats}, "
            f"showtimes_counts={showtimes_count}, seats_count={seats_count})>"
        )
