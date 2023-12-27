
"""Dummy Data for testing"""
import uuid
import datetime as dt
from typing import List, Tuple, Type, Dict, Any
from database.models import *

ModelType = Type[Base]
NIL_UUID = uuid.UUID("00000000-0000-0000-0000-000000000000")

DUMMY_DATA: List[Tuple[ModelType, Dict[str, Any]]] = [
    (
        Admin,
        {
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
        Movie,
        {
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
        Hall,
        {
            "name": "East Hall",
            "total_seats": 80
        }
    ),
    (
        ShowTime,
        {
            "show_date": dt.date(2023, 12, 26),
            "start_time": dt.time(20, 0),
            "end_time": dt.time(22, 23),
            "admin_id": NIL_UUID,
            "movie_id": NIL_UUID,
            "hall_id": NIL_UUID
        }
    ),
    (
        Booking,
        {
            "num_seats": 2,
            "status": 1,  # confirmed
            "order_total": 60.0,
            "customer_id": NIL_UUID,
            "staff_member_id": NIL_UUID,
            "showtime_id": NIL_UUID
        }
    ),
    (
        Seat,
        {
            "seat_name": "A1",
            "seat_type": "Regular",
            "is_reserved": True,
            "seat_price": 30.0,
            "booking_id": NIL_UUID,
            "hall_id": NIL_UUID
        }
    ),
    (
        Notification,
        {
            "content": "Ticket booked.",
            "booking_id": NIL_UUID,
            "customer_id": NIL_UUID
        }
    ),
    # (
    #     CreditCard,
    #     {
    #         "amount": 30.0,
    #         "credit_card_number": "1111222233334444",
    #         "expiry_date": dt.date(2024, 6, 1),
    #         "name_on_card": "Lil"
    #     }
    # ),
    # (
    #     Coupon,
    #     {
    #         "expiry_date": dt.date(2024, 6, 1),
    #         "discount": 50.0,
    #         "credit_card_id": NIL_UUID,
    #         "debit_card_id": None
    #     }
    # )
]
