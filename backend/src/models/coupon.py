"""Coupon models"""
from datetime import datetime as dt
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .payment import Payment


class Coupon(Payment):
    __tablename__ = "coupons"

    expiry_date: Mapped[dt.datetime]
    discount: Mapped[float]
