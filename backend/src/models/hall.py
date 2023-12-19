"""Create Hall model"""
from sqlalchemy.orm import Mapped
from database.db_init import BaseModel


class Hall(BaseModel):
    __tablename__ = "halls"

    name: Mapped[str]
    total_seats: Mapped[int]