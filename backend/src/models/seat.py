"""Create Seat model"""
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel


class Seat(BaseModel):
    __tablename__ = "seats"

    seat_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)
    seat_type: Mapped[int] = mapped_column(nullable=False)
    is_reserved: Mapped[bool] = mapped_column(nullable=False)
    seat_price: Mapped[float] = mapped_column(nullable=False)