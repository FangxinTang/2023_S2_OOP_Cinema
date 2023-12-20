"""Create Booking model"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel


class Booking(BaseModel):
    __tablename__ = "bookings"

    num_seats: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False, default=1)
    order_total: Mapped[float] = mapped_column(nullable=False)

    customer_id = mapped_column(ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="bookings")

    staff_id = mapped_column(ForeignKey("staff.id"))
    staff = relationship("Staff", back_populates="bookings")

    showtime_id = mapped_column(ForeignKey('showtime.id'))
    showtime = relationship('ShowTime', back_populates="bookings")