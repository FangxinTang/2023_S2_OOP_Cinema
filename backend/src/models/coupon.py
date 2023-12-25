# """Initialize the database"""
# import datetime as dt
# from sqlalchemy.orm import Mapped, mapped_column
# from models.base_model import BaseModel

    
# class Coupon(BaseModel):
#     __tablename__ = "coupons"

#     expiry_date: Mapped[dt.datetime] = mapped_column(nullable=False)
#     discount: Mapped[float] = mapped_column(nullable=False)

    # credit_card_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('credit_cards.id'), nullable=True)
    # credit_card: Mapped['CreditCard'] = relationship('CreditCard', back_populates='coupon', uselist=False)

    # debit_card_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('debit_cards.id'), nullable=True)
    # debit_card: Mapped['DebitCard'] = relationship('DebitCard', back_populates='coupon', uselist=False)

    # def __repr__(self):
    #     credit_card_info = f"credit_card_number='****{self.credit_card.credit_card_number[-4:]}'" if self.credit_card else "No CreditCard"
    #     debit_card_info = f"debit_card_number='****{self.debit_card.debit_card_number[-4:]}'" if self.debit_card else "No DebitCard"
    #     return (f"<Coupon(expiry_date={self.expiry_date}, discount={self.discount}, credit_card_info={credit_card_info}, debit_card_info={debit_card_info})>")
