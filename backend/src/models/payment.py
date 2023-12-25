"""Payment Abstract"""
from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from models.base_model import BaseModel


class Payment(BaseModel):
    __abstract__ = True

    amount: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationship with Booking: 1 to 1:
    @declared_attr
    def booking_id(cls):
        return mapped_column(ForeignKey('bookings.id'), nullable=False)
    
    @declared_attr
    def booking(cls):
        return relationship('Booking', back_populates='payment')


    # Relationship with Coupon: 1 to 1:
    @declared_attr
    def coupon_id(cls):
        return mapped_column(ForeignKey('coupons.id'), nullable=True)
    
    @declared_attr
    def coupon(cls):
        return relationship('Coupon', back_populates='payment', uselist=False)

    def __repr__(self):
        booking_info = f"Booking ID: {self.booking_id}" if self.booking_id else "No Booking"
        coupon_info = f"Coupon ID: {self.coupon_id}" if self.coupon else "No Coupon"
        return (f"<Payment(amount={self.amount}, {booking_info}, {coupon_info})>")
