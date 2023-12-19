"""Payment(Abstract) models"""
from sqlalchemy.orm import Mapped, mapped_column
from database.db_init import BaseModel # import from an external package

class Payment(BaseModel):
    __abstract__ = True

    amount: Mapped[float] = mapped_column(nullable=False)
