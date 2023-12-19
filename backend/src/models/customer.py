"""Create Customer model"""
from typing import List
from sqlalchemy.orm import relationship
from .user import User



class Customer(User):
    __tablename__ = "customers"

    booking = relationship("Booking", back_populates="customers")
    notification = relationship("Notification", back_populates="customers")