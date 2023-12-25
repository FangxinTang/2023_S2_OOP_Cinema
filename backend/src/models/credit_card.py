# """CreditCard Model"""
# import datetime as dt
# from typing_extensions import Annotated
# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column
# from models.payment import Payment



# BankCardUniqueString = Annotated[str,
#     mapped_column(String(200), nullable=False, unique=True)]

# class CreditCard(Payment):
#     __tablename__ = "credit_cards"

#     credit_card_number: Mapped[BankCardUniqueString]
#     expiry_date: Mapped[dt.date]
#     name_on_card : Mapped[str] = mapped_column(String(200), nullable=False)

#     # coupon_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('coupons.id'), nullable=True)
#     # coupon = relationship('Coupon', back_populates='credit_card', uselist=False)

#     # def __repr__(self):
#     #     payment_repr = super().__repr__()
#     #     return (
#     #         f"<CreditCard(\n {payment_repr}, "
#     #         f"credit_card_number='****{self.credit_card_number[-4:]}', "
#     #         f"expiry_date={self.expiry_date}, name_on_card='{self.name_on_card}')>"
#         # )