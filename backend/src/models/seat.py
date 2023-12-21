"""Create Seat model"""
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel
from .booking import Booking
from .hall import Hall

class Seat(BaseModel):
    __tablename__ = "seats"

    seat_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)
    seat_type: Mapped[int] = mapped_column(nullable=False)
    is_reserved: Mapped[bool] = mapped_column(nullable=False)
    seat_price: Mapped[float] = mapped_column(nullable=False)

    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'))
    booking: Mapped['Booking'] = relationship(back_populates='seats')

    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('halls.id'))
    hall: Mapped['Hall'] = relationship(back_populates='seats')