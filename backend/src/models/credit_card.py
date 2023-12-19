"""CreditCard models"""
from datetime import datetime as dt
from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .payment import Payment


bank_card_unique_string = Annotated[
    str,
    mapped_column(String(128),
                  nullable=False,
                  unique=True)
]

class CreditCard(Payment):
    __tablename__ = "credit_cards"

    credit_card_number: Mapped[bank_card_unique_string]
    expiry_date: Mapped[dt.datetime]
    name_on_card : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
