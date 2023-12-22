"""DebitCard models"""
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

class DebitCard(Payment):
    __tablename__ = "debit_cards"

    debit_card_number: Mapped[bank_card_unique_string]
    expiry_date: Mapped[dt.datetime]
    name_on_card : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )


    def __repr__(self):
        payment_repr = super().__repr__()
        return (
            f"<DebitCard(\n {payment_repr}, "
            f"debit_card_number='****{self.debit_card_number[-4:]}', "
            f"expiry_date={self.expiry_date}, name_on_card='{self.name_on_card}')>"
        )