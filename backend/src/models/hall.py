"""Create Hall model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from database.db_init import BaseModel
from .seat import Seat
from .showtime import ShowTime


class Hall(BaseModel):
    __tablename__ = "halls"

    name: Mapped[str]
    total_seats: Mapped[int]

    seats: Mapped[List['Seat']] = relationship(back_populates='hall')
    
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates='hall')