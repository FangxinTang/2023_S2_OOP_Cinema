"""Create Booking model"""
import uuid
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import BaseModel
# from .payment import Payment
# from .staff import Staff
# from .customer import Customer
# from .showtime import ShowTime
# from .notification import Notification
# from .seat import Seat


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

    def __repr__(self):
        seats_booked = len(self.seats) if self.seats else 0
        return (f"<Booking(num_seats={self.num_seats}, status={self.status}, order_total={self.order_total}, "
                f"customer_id={self.customer_id}, staff_member_id={self.staff_member_id}, "
                f"showtime_id={self.showtime_id}, seats_booked={seats_booked}, "
                f"payment_id={self.payment.id if self.payment else 'No payment'})>")
