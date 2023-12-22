"""Coupon models"""
from datetime import datetime as dt
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .payment import Payment


class Coupon(Payment):
    __tablename__ = "coupons"

    expiry_date: Mapped[dt.datetime] = mapped_column(nullable=False)
    discount: Mapped[float] = mapped_column(nullable=False)

    payment_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('payments.id'))
    payment: Mapped['Payment'] = relationship(back_populates='coupon')

    def __repr__(self):
        payment_info = f"Payment ID: {self.payment_id}" if self.payment_id else "No Payment"
        return (f"<Coupon(expiry_date={self.expiry_date}, discount={self.discount}, {payment_info})>")