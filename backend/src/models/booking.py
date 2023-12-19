"""Create Booking model"""
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel


class Booking(BaseModel):
    __tablename__ = "bookings"

    num_seats: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False, default=1)
    order_total: Mapped[float] = mapped_column(nullable=False)