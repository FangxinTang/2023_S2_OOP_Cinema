"""Initialize the database"""
import uuid
import datetime as dt

from typing import List
from typing_extensions import Annotated

from sqlalchemy import create_engine, String, Float, CheckConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship, declared_attr
from sqlalchemy.sql import func



engine = create_engine('postgresql://postgres:postgres@localhost/cinema', echo=True)
Base = declarative_base()



#################### Required String #####################
PersonRequiredUniqueString = Annotated[
    str,
    mapped_column(String(128), nullable=False, unique=True)]

UserRequiredUniqueString = Annotated[
    str,
    mapped_column(String(128), nullable=False, unique=True)]

BankCardUniqueString = Annotated[
    str,
    mapped_column(String(200), nullable=False, unique=True)]


#################### Base Model #####################
class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )

    datetime_modified: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.now()
    )

    datetime_created: Mapped[dt.datetime] = mapped_column(
        nullable=False,
        server_default=func.now()
    )

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, key):
        return hasattr(self, key)

    def keys(self):
        items = self.__mapper__.attrs.keys()
        return items

    def get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)
        return default

    def items(self):
        return [(key, getattr(self, key)) for key in self.keys()]

    def values(self):
        return [getattr(self, key) for key in self.keys()]

    def __iter__(self):
        return iter(self.keys())


#################### Person (Abstract) Model #####################
class Person(BaseModel):
    """Abstract base class representing a person."""

    __abstract__ = True

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[PersonRequiredUniqueString]
    phone: Mapped[PersonRequiredUniqueString]

    # Define address components as individual columns
    address_line_1: Mapped[str] = mapped_column(String(255))
    address_line_2: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(128))

    def __repr__(self):
        """Return a string representation of the Person object."""
        address = f"{self.address_line_1}, {self.address_line_2}, {self.country}"
        return f"<Person(\n name={self.name}, email={self.email}, phone={self.phone}, address={address}')>"


#################### User (Abstract) Model #####################
class User(Person):
    """Abstract base class representing a user with unique username and password."""
    __abstract__ = True

    username: Mapped[UserRequiredUniqueString]
    password: Mapped[UserRequiredUniqueString]

    def __repr__(self):
        person_repr = super().__repr__()
        return f"<User(\n {person_repr},\n username={self.username}\n)>"


#################### Admin Model #####################
class Admin(User):
    __tablename__ = "admins"

    # one-to-many 
    movies: Mapped[List['Movie']] = relationship(back_populates="admin")
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates="admin")

    def __repr__(self):
        user_repr = super().__repr__()
        movies_count = len(self.movies) if self.movies else 0
        showtimes_count = len(self.showtimes) if self.showtimes else 0

        return f"<Admin(\n {user_repr},\n movies_count={movies_count},\n showtimes_count={showtimes_count})>"


#################### Staff Model #####################
class Staff(User):
    __tablename__ = "staff_members"

    bookings: Mapped[List['Booking']] = relationship(back_populates="staff_member")

    def __repr__(self):
        user_repr = super().__repr__()
        bookings_count = len(self.bookings) if self.bookings else 0

        return f"<Staff(\n {user_repr},\n bookings_count={bookings_count})>"


#################### Customer Model #####################
class Customer(User):
    __tablename__ = "customers"

    bookings: Mapped[List['Booking']] = relationship(back_populates="customer")
    notifications: Mapped[List['Notification']] = relationship(back_populates="customer")

    def __repr__(self):
        user_repr = super().__repr__()
        bookings_count = len(self.bookings) if self.bookings else 0
        notifications_count = len(self.notifications) if self.notifications else 0

        return f"<Customer(\n {user_repr},\n bookings_count={bookings_count}, \n notifications_count={notifications_count})>"


#################### Notification Model #####################
class Notification(BaseModel):
    __tablename__ = "notifications"

    content: Mapped[str] = mapped_column(String(200), nullable=False)

    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped['Customer'] = relationship(back_populates="notifications")

    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'))
    booking: Mapped['Booking'] = relationship(back_populates='notifications')

    def __repr__(self):
        return f"<Notification\n (content={self.content}, customer={self.customer.name}, booking_id={self.booking.id})>"


#################### Movie Model #####################
class Movie(BaseModel):
    """Representing a movie in the database."""
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        unique=True
    )

    description: Mapped[str] = mapped_column(
        String(150),
        nullable=True
    )

    duration_mins: Mapped[int] = mapped_column(
        nullable=True,
        default=120
    )

    language: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
        default="English"
    )

    release_date: Mapped[dt.date] = mapped_column(
        nullable=True
    )

    country: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    genre: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            'duration_mins > 30 AND duration_mins < 250',
            name='duration_mins_range'
        ),
    )

    # many-to-one
    admin_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('admins.id'))
    admin: Mapped['Admin'] = relationship(back_populates='movies')

    # one-to-many
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates="movie")

    def __repr__(self):
        admin_name = self.admin.name if self.admin else None
        showtimes_count = len(self.showtimes) if self.showtimes else 0
        return(f"<Moive(\n" 
               f"  title='{self.title}'\n"
               f"  duration_min={self.duration_mins},\n"
               f"  language='{self.language}',\n"
               f"  release_date={self.release_date},\n"
               f"  country='{self.country},\n "
               f"  genre='{self.genre}',\n"
               f"  admin= {admin_name},\n"
               f"  showtimes_count={showtimes_count}>")
    

#################### Showtime Model #####################
class ShowTime(BaseModel):
    __tablename__ = "showtimes"

    show_date: Mapped[dt.date] = mapped_column(nullable=True)
    start_time: Mapped[dt.time] = mapped_column(nullable=True)
    end_time: Mapped[dt.time] = mapped_column(nullable=True)

    # Relationship with Admin - Many to one
    admin_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("admins.id"))
    admin: Mapped['Admin'] = relationship(back_populates="showtimes")

    # Relationship with Movie - Many to one
    movie_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('movies.id'))
    movie: Mapped['Movie'] = relationship(back_populates="showtimes")

    # Relationship with Hall - Many to one
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('halls.id'))
    hall: Mapped['Hall'] = relationship(back_populates='showtimes')

    # Relationship with Booking - One to many
    bookings: Mapped[List['Booking']] = relationship(back_populates='showtime')

    def __repr__(self):
        admin_name = self.admin.name if self.admin else 'No admin'
        movie_title = self.movie.title if self.movie else 'No movie'
        hall_name = self.hall.name if self.hall else 'No hall'
        bookings_count = len(self.bookings) if self.bookings else 0
        
        return (f"<ShowTime(\n"
            f"  show_date={self.show_date},\n"
            f"  start_time={self.start_time},\n"
            f"  end_date={self.end_time},\n"
            f"  admin={admin_name},\n"
            f"  movie_title={movie_title},\n"
            f"  hall={hall_name},\n"
            f"  bookings_count={bookings_count}\n)>")


#################### Hall Model #####################
class Hall(BaseModel):
    __tablename__ = "halls"

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)

    # Relationship with ShowTime: 1 to many
    showtimes: Mapped[List['ShowTime']] = relationship(back_populates='hall')

    # Relationship with Seat: 1 to Many
    seats: Mapped[List['Seat']] = relationship(back_populates='hall')

    def __repr__(self):
        showtimes_count = len(self.showtimes) if self.showtimes else 0
        seats_count = len(self.seats) if self.seats else 0
        return (
            f"<Hall(\n name={self.name}, total_seats={self.total_seats}, "
            f"showtimes_counts={showtimes_count}, seats_count={seats_count})>"
        )


#################### Seat Model #####################
class Seat(BaseModel):
    __tablename__ = "seats"

    seat_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    total_seats: Mapped[int] = mapped_column(nullable=False)
    seat_type: Mapped[int] = mapped_column(nullable=False)
    is_reserved: Mapped[bool] = mapped_column(nullable=False)
    seat_price: Mapped[float] = mapped_column(nullable=False)

    # Relationship with Booking: Many to 1
    booking_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('bookings.id'))
    booking: Mapped['Booking'] = relationship(back_populates='seats')

    # Relationship with Hall: Many to 1
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('halls.id'))
    hall: Mapped['Hall'] = relationship(back_populates='seats')

    def __repr__(self):
        booking_status = "Booked" if self.booking_id else "Available"
        hall_name = self.hall.name if self.hall_id else "Not booked"
        return (
            f"<Seat\n (seat_name={self.seat_name}, seat_type={self.seat_type}, "
            f"seat_price={self.seat_price}, booking_status={booking_status}, hall_name={hall_name})>"
        )


#################### Booking Model #####################
class Booking(BaseModel):
    __tablename__ = "bookings"

    num_seats: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False, default=1)
    order_total: Mapped[float] = mapped_column(nullable=False)

    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped['Customer'] = relationship(back_populates="bookings")

    staff_member_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("staff_members.id"))
    staff_member: Mapped['Staff'] = relationship(back_populates="bookings")

    showtime_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('showtimes.id'))
    showtime: Mapped['ShowTime'] = relationship(back_populates="bookings")

    notifications: Mapped[List['Notification']] = relationship(back_populates='booking')

    seats: Mapped[List['Seat']] = relationship(back_populates='booking')

    payment: Mapped['Payment'] = relationship(back_populates='booking')

    def __repr__(self):
        seats_booked = len(self.seats) if self.seats else 0
        return (f"<Booking(num_seats={self.num_seats}, status={self.status}, order_total={self.order_total}, "
                f"customer_id={self.customer_id}, staff_member_id={self.staff_member_id}, "
                f"showtime_id={self.showtime_id}, seats_booked={seats_booked}, "
                f"payment_id={self.payment.id if self.payment else 'No payment'})>")


#################### Payment(Abstract) Model #####################
class Payment(BaseModel):
    __abstract__ = True

    amount: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationship with Booking: 1 to 1:
    @declared_attr
    def booking_id(cls):
        return mapped_column(ForeignKey('bookings.id'), nullable=False)
    
    @declared_attr
    def booking(cls):
        return relationship('Booking', back_populates='payment')


    # Relationship with Coupon: 1 to 1:
    @declared_attr
    def coupon_id(cls):
        return mapped_column(ForeignKey('coupons.id'), nullable=True)
    
    @declared_attr
    def coupon(cls):
        return relationship('Coupon', back_populates='payment', uselist=False)

    def __repr__(self):
        booking_info = f"Booking ID: {self.booking_id}" if self.booking_id else "No Booking"
        coupon_info = f"Coupon ID: {self.coupon.id}" if self.coupon else "No Coupon"
        return (f"<Payment(amount={self.amount}, {booking_info}, {coupon_info})>")


#################### CreditCard Model #####################
class CreditCard(Payment):
    __tablename__ = "credit_cards"

    credit_card_number: Mapped[BankCardUniqueString]
    expiry_date: Mapped[dt.date]
    name_on_card : Mapped[str] = mapped_column(String(200), nullable=False)

    # coupon = relationship('Coupon', back_populates='credit_card', uselist=False)

    def __repr__(self):
        payment_repr = super().__repr__()
        return (
            f"<CreditCard(\n {payment_repr}, "
            f"credit_card_number='****{self.credit_card_number[-4:]}', "
            f"expiry_date={self.expiry_date}, name_on_card='{self.name_on_card}')>"
        )


#################### DebitCard Model #####################
class DebitCard(Payment):
    __tablename__ = "debit_cards"

    debit_card_number: Mapped[BankCardUniqueString]
    expiry_date: Mapped[dt.date]
    name_on_card : Mapped[str] = mapped_column(String(200), nullable=False)

    # coupon = relationship('Coupon', back_populates='debit_card', uselist=False)

    def __repr__(self):
        payment_repr = super().__repr__()
        return (
            f"<DebitCard(\n {payment_repr}, "
            f"debit_card_number='****{self.debit_card_number[-4:]}', "
            f"expiry_date={self.expiry_date}, name_on_card='{self.name_on_card}')>"
        )


#################### Coupon Model #####################
class Coupon(BaseModel):
    __tablename__ = "coupons"

    expiry_date: Mapped[dt.datetime] = mapped_column(nullable=False)
    discount: Mapped[float] = mapped_column(nullable=False)

    # credit_card_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('credit_cards.id'), nullable=True)
    # credit_card: Mapped['CreditCard'] = relationship('CreditCard', back_populates='coupon', uselist=False)

    # debit_card_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('debit_cards.id'), nullable=True)
    # debit_card: Mapped['DebitCard'] = relationship('DebitCard', back_populates='coupon', uselist=False)

    def __repr__(self):
        # credit_card_info = f"credit_card_number='****{self.credit_card.credit_card_number[-4:]}'" if self.credit_card else "No CreditCard"
        # debit_card_info = f"debit_card_number='****{self.debit_card.debit_card_number[-4:]}'" if self.debit_card else "No DebitCard"
        return (f"<Coupon(expiry_date={self.expiry_date}, discount={self.discount})>")

######################
    

# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
