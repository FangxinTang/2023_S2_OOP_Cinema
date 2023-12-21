"""Create Booking model"""
import uuid
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel
from .payment import Payment
from .staff import Staff
from .customer import Customer
from .showtime import ShowTime
from .notification import Notification
from .seat import Seat


class Booking(BaseModel):
    __tablename__ = "bookings"

    num_seats: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False, default=1)
    order_total: Mapped[float] = mapped_column(nullable=False)

    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped['Customer'] = relationship(back_populates="bookings")

    staff_member_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("staff_members.id"))
    staff_member: Mapped['Staff'] = relationship(back_populates="bookings")

    showtime_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('showtimes.id'))
    showtime: Mapped['ShowTime'] = relationship(back_populates="bookings")

    notifications: Mapped[List['Notification']] = relationship(back_populates='booking')

    seats: Mapped[List['Seat']] = relationship(back_populates='booking')

    payment: Mapped['Payment'] = relationship(back_populates='booking')

    