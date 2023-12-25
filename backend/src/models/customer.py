"""Customer Model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from models.user import User


class Customer(User):
    __tablename__ = "customers"

    bookings: Mapped[List['Booking']] = relationship(back_populates="customer")
    notifications: Mapped[List['Notification']] = relationship(back_populates="customer")

    def __repr__(self):
        user_repr = super().__repr__()
        bookings_count = len(self.bookings) if self.bookings else 0
        notifications_count = len(self.notifications) if self.notifications else 0

        return f"<Customer(\n {user_repr},\n bookings_count={bookings_count}, \n notifications_count={notifications_count})>"