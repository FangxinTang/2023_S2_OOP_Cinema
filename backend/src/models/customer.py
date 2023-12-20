"""Create Customer model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from .notification import Notification
from .booking import Booking
from .user import User



class Customer(User):
    __tablename__ = "customers"

    bookings: Mapped[List['Booking']] = relationship("Booking", back_populates="customers")
    notifications: Mapped[List['Notification']] = relationship("Notification", back_populates="customers")