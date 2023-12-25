"""Notification Model"""
import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_model import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    content: Mapped[str] = mapped_column(String(200), nullable=False)

    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped['Customer'] = relationship(back_populates="notifications")

    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'))
    booking: Mapped['Booking'] = relationship(back_populates='notifications')

    def __repr__(self):
        return f"<Notification\n (content={self.content}, customer={self.customer.name}, booking_id={self.booking.id})>"
