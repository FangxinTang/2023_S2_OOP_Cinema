"""Create Notification model"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    content: Mapped[str] = mapped_column(String(200), nullable=False)