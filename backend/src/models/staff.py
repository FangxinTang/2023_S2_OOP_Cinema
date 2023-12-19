"""Create Staff model"""
from sqlalchemy.orm import relationship
from .user import User


class Staff(User):
    __tablename__ = "staff"

    bookings = relationship("Booking", back_populates="staff_member")