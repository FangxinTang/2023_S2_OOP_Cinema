"""Create Seat model"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel


class Seat(BaseModel):
    __tablename__ = "seats"

    seat_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)
    seat_type: Mapped[int] = mapped_column(nullable=False)
    is_reserved: Mapped[bool] = mapped_column(nullable=False)
    seat_price: Mapped[float] = mapped_column(nullable=False)

    booking_id = mapped_column(ForeignKey('booking.id'))
    booking = relationship('Booking', back_populates='seats')

    hall_id = mapped_column(ForeignKey('hall.id'))
    hall = relationship('Hall', back_populates='seats')