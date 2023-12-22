"""Payment(Abstract) models"""
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel
from .booking import Booking
from .coupon import Coupon


class Payment(BaseModel):
    __abstract__ = True

    amount: Mapped[float] = mapped_column(nullable=False)

    # Relationship with Booking: 1 to 1:
    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'))
    booking: Mapped['Booking'] = relationship(back_populates='payment')

    # Relationship with Coupon: 1 to 1:
    coupon: Mapped['Coupon'] = relationship(back_populates='payment')

    def __repr__(self):
        booking_info = f"Booking ID: {self.booking_id}" if self.booking_id else "No Booking"
        coupon_info = f"Coupon ID: {self.coupon.id}" if self.coupon else "No Coupon"
        return (f"<Payment(amount={self.amount}, {booking_info}, {coupon_info})>")
