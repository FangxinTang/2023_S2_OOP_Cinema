## 
# @file models.py
#
# @brief this is the models 
#
# @section author_cinemas Author
# Created by Fangxin Tang on 27/09/2023

# Imports

from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime, date, time

############################# 1.Cinema #############################
class Cinema:
    """This CinemaInfo class is to create a cinema instance."""

    def __init__(
            self,
            name: str, 
            total_halls: int, 
            total_seats: int, 
            location: str) -> None:

        self._name = name
        self._total_halls = total_halls
        self._total_seats = total_seats
        self._location = location

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def total_halls(self) -> int:
        return self._total_halls

    @total_halls.setter
    def total_halls(self, value: int) -> None:
        self._total_halls = value

    @property
    def total_seats(self) -> int:
        return self._total_seats
    
    @total_seats.setter
    def total_seats(self, value: int) -> None:
        self._total_seats = value

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, value: str) -> None:
        self._location = value
    
    def __str__(self):
        return f"Cinema Name: {self.name}, Location: {self.location}, Total Halls: {self.total_halls}, Total Seats: {self.total_seats}"

############################# 2.CinemaHall #############################
class CinemaHall:

    def __init__(self, name:str, capacity:int):
        self._name=name
        self._capacity = capacity
        self.seats = []
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def capacity(self) -> int:
        """Getter for the capacity attribute."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """Setter for the capacity attribute."""
        if isinstance(value, int) and value > 0:
            self._capacity = value
        else:
            print("Capacity must be a positive integer.")

    def __str__(self):
        return f"Hall Capacity - {self._capacity}\nSeats - {self.seats}\n"

############################# 3.HallSeat #############################
class HallSeat:
    
    def __init__(self, seat_type: str = None, price: float = 0.0, is_available = True):
        self._seat_type = seat_type
        self._price = price
        self._is_available = is_available

    @property
    def seat_type(self) -> str:
        """Getter for seat_type attribute."""
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value: str) -> None:
        """Setter for seat_type attribute."""
        self._seat_type = value

    @property
    def price(self) -> float:
        """Getter for price attribute."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Setter for price attribute."""
        self._price = value

    @property
    def is_available(self) -> bool:
        return self._is_available
    
    @is_available.setter
    def is_available(self, value: bool):
        self._is_available = value
    
    def __str__(self):
        """Get information about the seat."""
        availability = "Yes" if self.is_available else "No"
        return f"\
            Seat type: {self.seat_type};\
            Price: {self.price}; \
            Availability: {availability};\n"

############################# 4.Movie #############################
class Movie:
    """!This is the Movie Class"""
    def __init__(self, title:str, description:str, duration_mins:int, language:str, country:str, genre:str, release_date:datetime):
        self._title = title
        self._description= description
        self._duration_mins=duration_mins
        self._language=language
        self._country = country
        self._genre = genre
        self._release_date = release_date
        self._screenings_list = []

    @property
    def title(self) -> str:
        """Getter for title attribute."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Setter for title attribute."""
        self._title = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def duration_mins(self) -> int:
        return self._duration_mins

    @duration_mins.setter
    def duration_mins(self, value: str) -> None:
        self._duration_mins = value

    @property
    def language(self) -> str:
        """Getter for language attribute."""
        return self._language

    @language.setter
    def language(self, value: str) -> None:
        """Setter for language attribute."""
        self._language = value

    @property
    def genre(self) -> str:
        """Getter for genre attribute."""
        return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        """Setter for genre attribute."""
        self._genre = value

    @property
    def release_date(self) -> datetime:
        """Getter for release_date attribute."""
        return self._release_date

    @release_date.setter
    def release_date(self, value: datetime) -> None:
        """Setter for release_date attribute."""
        self._release_date = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str) -> None:
        self._country = value


    def get_screenings_list(self):
        return self.screenings_list


    def __str__(self) -> str:
        info = f"Title: {self.title}\n\
                Description: {self.description}\n\
                Language: {self.language}\n\
                Genre: {self.genre}\n\
                Release Date: {self.release_date}\n\
                Country: {self.country}\n\
                Duration: {self.duration_mins}"
        return info

############################# 5.Screening #############################
class Screening:
    """!The Screening class"""

    def __init__(self, hall_id:int, screening_date:datetime, start_time:datetime, end_time:datetime) -> None:
        self._hall_id = hall_id
        self._screening_date = screening_date
        self._start_time = start_time
        self._end_time = end_time

    @property
    def hall_id(self):
        return self._hall_id
    
    @property
    def screening_date(self):
        return self._screening_date
    
    @screening_date.setter
    def screening_date(self, value:datetime):
        self._screening_date = value

    @property
    def start_time(self) -> datetime:
        """Getter for start_time attribute."""
        return self._start_time

    @start_time.setter
    def start_time(self, value: datetime) -> None:
        """Setter for start_time attribute."""
        self._start_time = value

    @property
    def end_time(self) -> datetime:
        """Getter for end_time attribute."""
        return self._end_time

    @end_time.setter
    def end_time(self, value: datetime) -> None:
        """Setter for end_time attribute."""
        self._end_time = value

    def info(self) -> str:
        return f"Screening ID: {self.screening_id}, Movie: {self.movie.info()}, Hall: {self.hall.info()}, Start Time: {self.start_time}, End Time: {self.end_time}"


############################# 6.User #############################
class User(ABC):
    """! The User class"""

    next_id = 1

    def __init__(self,fname: str, lname: str, username: str, password: str):
        """!
        The initializer for User. It is to assign an id to an user object.

        @param fname The first name of the user.
        @param lname The last name of the user.
        @param username The username of the user.
        @param password The password of the user.
        @attribute id(int) The unique identifier of the user
        """
        self._id = User.next_id
        User.next_id += 1
        self._fname = fname
        self._lname = lname
        self._username = username
        self._password = password

    # Getters and Setters
    @property
    def id(self):
        return self._id

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, new_fname):
        self._fname = new_fname

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, new_lname):
        self._lname = new_lname

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        """!Reset the user's password."""
        self._password = new_password

    def construct_full_name(self)->str:
        """!Get the full name of the user, capitalized.
        @returns The string of the user's full name with both first name and last name capitalized.
        """
        full_name = f"{self.fname.capitalize()} {self.lname.capitalize()}"
        return full_name

    @abstractmethod
    def info(self)->str:
        return f"\
            Full Name : {self.construct_full_name()}\n\
            User ID: {self.username}\n"


############################# 7.Customer #############################
class Customer(User):  
    next_id = 100
    def __init__(self, fname: str, lname: str, username: str, password: str):
        self._customer_id = Customer.next_id
        Customer.next_id += 1
        self._booking = []## List to store booking information
        
        super().__init__(fname, lname, username, password)
        
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def bookings(self):
        return self._bookings

    @bookings.setter
    def bookings(self, new_bookings:List[dict]):
        self._bookings = new_bookings


    def make_booking(self, booking_details:dict) -> str:
        """!Make a booking and add it to the booking list.
        @param booking_details Details of the booking, e.g., movie, screening, seats, payment.
        """
        booking_id = len(self.bookings) + 1
        booking_details["booking_id"] = booking_id
        self.bookings.append(booking_details)
        return f"Booking successful! Booking ID: {booking_id}"

    def remove_booking(self, booking_id: int):
        """!Cancel a booking from the booking list.
        @param booking_id: The unique identifier of the booking to be canceled.
        """
        for booking in self.bookings:
            if booking.get("booking_id") == booking_id:
                self.bookings.remove(booking)
                print(f"Booking ID {booking_id} canceled.")
                break
        else:
            print(f"Booking ID {booking_id} not found.")

    def info(self)->str:
        """!Get information about the customer.
        @return Information about the cusotmer in string format"""
        return f"Customer ID: {self.customer_id}, Full Name: {self.construct_full_name()}, Bookings: {len(self.bookings)}"


############################# 8.Staff #############################
class Staff(User):  
    """!The Staff class, inherits from User"""
    next_id = 1

    def __init__(self, role: int, fname: str, lname: str, username: str, password: str):
        """!
        The initializer for Staff.
        @param fname The first name of the staff.
        @param lname The last name of the staff.
        @param username The username of the staff.
        @param password The password of the staff.
        @param role The role of staff where 1 indicates admin and 0 indicates receiptionist.
        @attribute staff_id The unique identifier of the staff.
        """
        self._staff_id = Staff.next_id
        Staff.next_id += 1

        super().__init__(fname, lname, username, password)
        self._role = role
        
    @property
    def staff_id(self) -> int:
        """Getter for staff_id attribute."""
        return self._staff_id

    @property
    def role(self) -> int:
        """Getter for role attribute."""
        return self._role

    @role.setter
    def role(self, value: int) -> None:
        """Setter for role attribute."""
        self._role = value

    def info(self) -> str:
        """Get information about the staff."""
        return f"Staff ID: {self.staff_id}, Full Name: {self.construct_full_name()}, Role: {'Admin' if self.role == 1 else 'Receptionist'}"


############################# 9.Admin #############################
class Admin(Staff):  
    """!The Admin class, inherits from Staff"""
    def __init__(self, role: int, fname: str, lname: str, username: str, password: str):
        """!
        The initializer for Admin.

        @param fname The first name of the staff.
        @param lname The last name of the staff.
        @param username The username of the staff.
        @param password The password of the staff.
        @param role The role of staff where 1 indicates admin and 0 indicates receiptionist.
        @attribute staff_id The unique identifier of the staff.
        """
        # Admin role is set to 1
        super().__init__(role=1, fname=fname, lname=lname, username=username, password=password)

    def add_movie(self, movie_details: dict):
        """!Add a new movie to the cinema's movie list.
        @param movie_details Details of the movie, e.g., title, genre, release date.
        """
        pass


    def remove_movie(self, movie_id: int):
        """!Remove a movie from the cinema's movie list.
        @param movie_id: The unique identifier of the movie to be removed.
        """
        pass


    def add_screening(self, screening_details: dict):
        """!Add a new screening to the cinema's screening schedule.
        @param screening_details Details of the screening, e.g., movie, hall, date, time, etc.
        """
        pass


    def cancel_screening(self, screening_id: int):
        """!Cancel a screening from the cinema's screening schedule.
        @param screening_id The unique identifier of the screening to be canceled.
        """
        pass


    def info(self) -> str:
        """!Get information about the admin.
        @return: Information about the admin.
        """
        return f"Admin ID: {self.staff_id}, Full Name: {self.construct_full_name()}"


############################# 10.Receiptionist #############################
class Receiptionist(Staff):  
    """!The Receiptionist class, inherits from Staff"""
   
    def __init__(self, role: int, fname: str, lname: str, username: str, password: str):
        """!
        The initializer for Receiptionist.
        @param fname The first name of the staff.
        @param lname The last name of the staff.
        @param username The username of the staff.
        @param password The password of the staff.
        @param role The role of staff where 1 indicates admin and 0 indicates receiptionist.
        @attribute staff_id The unique identifier of the staff.
        """
        super().__init__(role=0, fname=fname, lname=lname, username=username, password=password)

    def create_booking(self, booking_details: dict):
        """!Create a new booking for a customer.
        @param booking_details: Details of the booking, e.g., customer, movie, screening, seats, etc.
        """
        pass

    def cancel_booking(self, booking_id: int):
        """!Cancel a booking for a customer.
        @param booking_id The unique identifier of the booking to be canceled.
        """
        pass

    def info(self) -> str:
        """!Get information about the receptionist.
        @return: Information about the receptionist.
        """
        return f"Receptionist ID: {self.staff_id}, Full Name: {self.construct_full_name()}"


############################# 11.Booking #############################
class Booking:
    """!The Booking class"""
    next_id = 1

    def __init__(self, 
                 num_seats:int, 
                 booking_datetime:datetime, 
                 booking_status:str, 
                 booked_by:User,
                 discount:float=0.0):
        """!Initialize a Booking object.
        @param num_seat The number of seats booked.
        @param booking_datetime The datetime when the booking was made.
        @param booking_status The status of the booking str.
        @param booked_by The User (Customer or Receptionist) who made the booking.
        @param discount The discount applied to the booking as a percentage, default is 0.0"""
        self._booking_id = Booking.next_id
        Booking.next_id += 1
        self._num_seats = num_seats
        self._booking_datetime = booking_datetime
        self._booking_status = booking_status
        self._booked_by = booked_by
        self._discount = discount

    @property
    def num_seats(self) -> int:
        """Getter for num_seats attribute."""
        return self._num_seats

    @property
    def booking_datetime(self) -> datetime:
        """Getter for booking_datetime attribute."""
        return self._booking_datetime

    @property
    def booking_status(self) -> str:
        """Getter for booking_status attribute."""
        return self._booking_status

    @property
    def booked_by(self) -> User:
        """Getter for booked_by attribute."""
        return self._booked_by

    @property
    def discount(self) -> float:
        """Getter for discount attribute."""
        return self._discount
    
    def calc_total_amount(self, ticket_price:float):
        """!Calculate the total ticket price for the booking after applying the discount.
        @param ticket_price The base ticket price per seat.
        @return The total ticket price after applying the discount.
        """
        total_amount = self.num_seats * ticket_price * (1 - self.discount / 100)
        return total_amount
    
    def cancel_booking(self, booking_id:int):
        """!Cancel the booking by changing its status to Canceled
        @param booking_id The identifier of the booking to cancel"""
        self._booking_status = "Canceled"



############################# 12.Booking #############################
class Payment:
    """!The Payment class"""
    next_id = 1
    def __init__(self, amount:float, payment_datetime:datetime, booking_id:int):
        """!Initialize a Payment object.
        @param payment_id The unique identifier for the payment.
        @param amount The amount of the payment.
        @param payment_datetime The date and time when the payment was made.
        @param booking_id The unique identifier of the booking associated with the payment.
        """
        payment_id = Payment.next_id
        next_id += 1
        self._payment_id = Payment.next_id
        Payment.next_id += 1
        self._amount = amount
        self._payment_datetime = payment_datetime
        self._booking_id = booking_id

    @property
    def payment_id(self) -> int:
        """Getter for payment_id attribute."""
        return self._payment_id

    @property
    def amount(self) -> float:
        """Getter for amount attribute."""
        return self._amount

    @property
    def payment_datetime(self) -> datetime:
        """Getter for payment_datetime attribute."""
        return self._payment_datetime

    @property
    def booking_id(self) -> int:
        """Getter for booking_id attribute."""
        return self._booking_id
    
    def info(self) -> str:
        """Get the payment info.
        @return: The payment info.
        """
        return f"Payment ID: {self.payment_id}, Amount: {self.amount}, Payment Date: {self.payment_datetime}, Booking ID: {self.booking_id}"


############################# 13.Notification #############################
class Notification:
    """!The Notification class"""
    next_id = 1
    def __init__(self, send_datetime:datetime, content:str):
        """Initialize the Notification object"""
        self.notification_id = Notification.next_id
        Notification.next_id += 1
        self._send_datetime = send_datetime
        self._content = content

    @property
    def notification_id(self) -> int:
        """Getter for notification_id attribute."""
        return self._notification_id

    @property
    def send_datetime(self) -> datetime:
        """Getter for send_datetime attribute."""
        return self._send_datetime

    @property
    def content(self) -> str:
        """Getter for content attribute."""
        return self._content

    def send(self):
        """Send the notification."""
        print(f"Notification {self.notification_id} sent on {self.send_datetime}. Content: {self.content}")
