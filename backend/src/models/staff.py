"""Staff Model"""
from typing import List
from sqlalchemy.orm import Mapped, relationship
from models.user import User


class Staff(User):
    __tablename__ = "staff_members"

    bookings: Mapped[List['Booking']] = relationship(back_populates="staff_member")

    def __repr__(self):
        user_repr = super().__repr__()
        bookings_count = len(self.bookings) if self.bookings else 0

        return f"<Staff(\n {user_repr},\n bookings_count={bookings_count})>"
