"""Create Staff model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from .user import User
from .booking import Booking


class Staff(User):
    __tablename__ = "staff"

    bookings: Mapped[List['Booking']] = relationship("Booking", back_populates="staff_member")