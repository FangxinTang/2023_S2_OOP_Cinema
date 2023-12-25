import uuid
import datetime as dt
from typing import List, Tuple, Type, Dict, Any
from sqlalchemy.ext.declarative import DeclarativeMeta
from database.models import Admin, Staff, Customer, Notification, Movie, ShowTime, Hall, Seat, Booking, CreditCard, DebitCard, Coupon

ModelType = Type[DeclarativeMeta]
NIL_UUID = uuid.UUID("00000000-0000-0000-0000-000000000000")

DUMMY_DATA:List[Tuple[ModelType, Dict[str, Any]]] = [
    (
        Admin,
        {
            "id": NIL_UUID,
            "name": "Sam",
            "email": "sam@demo.com",
            "phone": "123456789",
            "address_line_1": "6 Puriri Avenue",
            "address_line_2": "Auckland",
            "country": "NZ",
            "username": "admin_sam",
            "password": "secretpassword"
        }
    ),
    (
        Staff,
        {
            "id": NIL_UUID,
            "name": "Mary",
            "email": "mary@demo.com",
            "phone": "223456789",
            "address_line_1": "15 Puriri Avenue",
            "address_line_2": "Auckland",
            "country": "NZ",
            "username": "staff_mary",
            "password": "secretpassword"
        }
    ),
    (
        Customer,
        {
            "id": NIL_UUID,
            "name": "Lil",
            "email": "lil@demo.com",
            "phone": "323456789",
            "address_line_1": "100 Puriri Avenue",
            "address_line_2": "Christchurch",
            "country": "NZ",
            "username": "customer_lil",
            "password": "secretpassword"
        }
    ),
    (
        Notification,
        {
            "id": NIL_UUID,
            "content": "Ticket booked.",
            "customer_id": NIL_UUID
        }
    ),
    (
        Movie,
        {
            "id": NIL_UUID,
            "title": "Aquaman 2",
            "description": "The sequel to the 2018 film 'Aquaman', following the title character's post-Justice League adventures.",
            "duration_mins": 143,
            "language": "English",
            "release_date": dt.date(2023, 12, 16),
            "country": "USA",
            "genre": "Adventure",
            "admin_id": NIL_UUID
        }
    ),
    (
        ShowTime,
        {
            "id": NIL_UUID,
            "show_date": dt.date(2023, 12, 26),
            "start_time": dt.time(20, 0),
            "end_time": dt.time(22, 23),
            "admin_id": NIL_UUID,
            "movie_id": NIL_UUID,
            "hall_id": NIL_UUID
        }
    ),
    (
        Hall,
        {
            "id": NIL_UUID,
            "name": "East Hall",
            "total_seats": 80
        }
    ),
    (
        Seat,
        {
            "id": NIL_UUID,
            "seat_name": "A1",
            "seat_type": "Regular",
            "is_reserved": True,
            "seat_price": 30.0,
            "booking_id": NIL_UUID,
            "hall_id": NIL_UUID
        }
    ),
    (
        Booking,
        {
            "id": NIL_UUID,
            "num_seats": 2,
            "status": 1, #confirmed
            "order_total": 60.0,
            "customer_id": NIL_UUID,
            "staff_member_id": NIL_UUID,
            "showtime_id": NIL_UUID
        }
    ),
    (
        CreditCard,
        {
            "id": NIL_UUID,
            "amount": 30.0,
            "credit_card_number": "1111222233334444",
            "expiry_date": dt.date(2024, 6),
            "name_on_card": "Lil"
        }
    ),
    (
        Coupon,
        {
            "id": NIL_UUID,
            "expiry_date": dt.date(2024, 6),
            "discount": 50.0,
            "credit_card_id": NIL_UUID,
            "debit_card_id": None
        }
    )
]