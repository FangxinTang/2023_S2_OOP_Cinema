"""Test"""
from sqlalchemy.orm import Mapped, mapped_column
from models.base_model import BaseModel

    
class Test(BaseModel):
    __tablename__ = "coupons"

    test_column: Mapped[str] = mapped_column(nullable=True)