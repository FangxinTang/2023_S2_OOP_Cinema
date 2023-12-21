"""Create Customer model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from .notification import Notification
from .booking import Booking
from .user import User



class Customer(User):
    __tablename__ = "customers"

    bookings: Mapped[List['Booking']] = relationship(back_populates="customer")
    notifications: Mapped[List['Notification']] = relationship(back_populates="customer")