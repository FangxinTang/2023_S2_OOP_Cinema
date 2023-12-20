"""Create Notification model"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    content: Mapped[str] = mapped_column(String(200), nullable=False)

    customer_id = mapped_column(ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="notifications")

    booking_id = mapped_column(ForeignKey('booking.id'))
    booking = relationship('Booking', back_populates='notifications')