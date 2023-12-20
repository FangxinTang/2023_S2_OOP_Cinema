"""Create Hall model"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel


class Hall(BaseModel):
    __tablename__ = "halls"

    name: Mapped[str]
    total_seats: Mapped[int]

    seats = relationship('Seat', back_populates='hall')
    
    showtimes = relationship('ShowTime', back_populates='hall')