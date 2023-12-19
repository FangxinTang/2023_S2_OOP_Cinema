"""Create tables"""
import sys
import pathlib as pl
from sqlalchemy.orm import sessionmaker


sys.path.insert(0, str(pl.Path(__file__).resolve().parent.parent))

from database.db_init import engine, Base
from models.person import Person
from models.user import User
from models.admin import Admin
from models.staff import Staff
from models.customer import Customer
from models.movies import Movie
from models.showtime import ShowTime
from models.booking import Booking
from models.hall import Hall
from models.seat import Seat
from models.notification import Notification
from models.payment import Payment
from models.credit_card import CreditCard
from models.debit_card import DebitCard
from models.coupon import Coupon


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)