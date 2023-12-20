"""Coupon models"""
from datetime import datetime as dt
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .payment import Payment


class Coupon(Payment):
    __tablename__ = "coupons"

    expiry_date: Mapped[dt.datetime]
    discount: Mapped[float]

    payment_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('payment.id'))
    payment: Mapped['Payment'] = relationship(back_populates='coupon')
