"""Seat Model"""
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_model import BaseModel


class Seat(BaseModel):
    __tablename__ = "seats"

    seat_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)
    seat_type: Mapped[int] = mapped_column(nullable=False)
    is_reserved: Mapped[bool] = mapped_column(nullable=False)
    seat_price: Mapped[float] = mapped_column(nullable=False)

    # Relationship with Booking: Many to 1
    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'))
    booking: Mapped['Booking'] = relationship(back_populates='seats')

    # Relationship with Hall: Many to 1
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('halls.id'))
    hall: Mapped['Hall'] = relationship(back_populates='seats')

    def __repr__(self):
        booking_status = "Booked" if self.booking_id else "Available"
        hall_name = self.hall.name if self.hall_id else "Not booked"
        return (
            f"<Seat\n (seat_name={self.seat_name}, seat_type={self.seat_type}, "
            f"seat_price={self.seat_price}, booking_status={booking_status}, hall_name={hall_name})>"
        )

