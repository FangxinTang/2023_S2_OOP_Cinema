"""Payment(Abstract) models"""
import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db_init import BaseModel
from .booking import Booking 

class Payment(BaseModel):
    __abstract__ = True

    amount: Mapped[float] = mapped_column(nullable=False)

    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('booking.id'))
    booking: Mapped['Booking'] = relationship(back_populates='payment')
