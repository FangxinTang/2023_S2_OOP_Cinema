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

class CinemaInfo:
    """!This CinemaInfo class is to create a cinema instance."""
    def __init__(self, name:str, total_halls:int, total_seats:int, location:str) -> None:
        """! Initializer for a new cinema object.
        @param name The name of the cinema, such as Lincoln Cinemas,
        @param total_halls The total number of halls, such as 4 halls, 
        @param total_seats The total number of seats in the cinema, such as 400 seats,
        @param location The localtion of the cinema, such as Location at Lincoln"""
        pass


class CinemaHall:
    """!CinemaHall class is to create a hall instance which contains the hall info."""
    next_hall_id = 1
    def __init__(self, capacity:int):
        """! Initializer for a new hall object and assign a hall_id to a hall,
        @param capacity The maximum capacity of the tall (total seats)  """
        self.hall_id = CinemaHall.next_hall_id
        CinemaHall.next_hall_id += 1

        self.capacity = capacity
        pass


class CinemaHallSeat:
    """!CinemaHallSeat class is to create seat instances within a cinema hall."""
    def __init__(self, seat_row:int, seat_column:int, seat_type:str):
        """!Initializer for a new CinemaHallSeat object
        @param seat_row The row number of the seat.
        @param seat_column The column number of the seat.
        @param seat_type The type of the seat, eg, Regular, Accessable, EmergencyExit, other"""
        pass


class ScreeningSeat:
    """!ScreeningSeat class is to create seat instances within a screening."""
    def __init__(self, seat_number:str, price:float, is_researved:bool):
        """!Initializer for a new ScreeningSeat object
        @param seat_number The seat number (e.g., "A1", "B3").
        @param price The price of the seat for a specific screening.
        @param is_reserved True if the seat is reserved, False if it is available."""
        pass



class Movie:
    """!This is the Movie Class"""
    next_id = 1
    def __init__(self, title:str, language:str, genre:str, release_date:str):
        """!
        Initializer for Movie object. Assign a movie id to the movie object.
        @param title Title of the movie.
        @param language Language of the movie.
        @param genre Genre of the movie.
        @param release_date The date this movie releases.
        """
        pass

    def info(self)->str:
        """!Get information about the movie.
        @return Information about the movie."""
        pass


class Screening:
    """!The Screening class"""
    next_id = 1
    def __init__(self, movie:Movie, hall:CinemaHall, date:date, start_time:time, end_time:time) -> None:
        """!Initialize a Screening object.
        @param movie: The Movie object being screened.
        @param hall: The Hall object where the screening takes place.
        @param date: The date of the screening.
        @param start_time: The start time of the screening.
        @param end_time: The end time of the screening.
        """
        pass

    def info()->str:
        """!Get a list of screenings related to the movie.
        @return A list of Screening objects for this movie.
        """



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
        ## This is the first name
        self._fname = fname
        ## This is the last name
        self._lname = lname
        ## This is the username
        self._username = username
        ## This is the password
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

    
    def verifyLogin(self)->bool:
        """!Verify if the user is logged in.
        @return True if the user is loggedin, False otherwise"""
        pass

    def construct_full_name(self)->str:
        """!Get the full name of the user, capitalized.
        @returns The string of the user's full name with both first name and last name capitalized.
        """
        full_name = f"{self.fname.capitalize()} {self.lname.capitalize()}"
        return full_name
    

    @abstractmethod
    def info(self)->str:
        """!Abstract method to get information about the user.
        @return Information about the user.
        """
        pass



class Customer(User):  
    """!The Customer class, inherits from User"""
    next_id = 100

    def __init__(self, fname: str, lname: str, username: str, password: str):
        """!
        The initializer for Customer.

        @param fname The first name of the customer.
        @param lname The last name of the customer.
        @param username The username of the customer.
        @param password The password of the customer.
        """
        ## @attribute customer_id(int) The unique identifier of the customer.
        self._customer_id = Customer.next_id
        Customer.next_id += 1
        ## List to store booking information
        super().__init__(fname, lname, username, password)
        self._bookings = []


    @property
    def customer_id(self):
        return self._customer_id
    
    
    @property
    def bookings(self):
        return self._bookings

    @bookings.setter
    def bookings(self, new_bookings):
        self._bookings = new_bookings


    def make_booking(self, booking_details:dict) -> str:
        """!Make a booking and add it to the booking list.
        @param booking_details Details of the booking, e.g., movie, screening, seats, payment.
        """
        pass

    def remove_booking(self, booking_id: int):
        """!Cancel a booking from the booking list.
        @param booking_id: The unique identifier of the booking to be canceled.
        """
        pass


    def info(self)->str:
        """!Get information about the customer.
        @return Information about the cusotmer in string format"""
        pass



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
        pass



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
        pass

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
        pass



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
        pass


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
        pass



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
        pass

    def calc_total_amount(self, ticket_price:float):
        """!Calculate the total ticket price for the booking after applying the discount.
        @param ticket_price The base ticket price per seat.
        @return The total ticket price after applying the discount.
        """

    def cancel_booking(self, booking_id:int):
        """!Cancel the booking by changing its status to Canceled
        @param booking_id The identifier of the booking to cancel"""
        pass



class Payment:
    """!The Payment class"""
    next_id = 1
    def __init__(self, amout:float, payment_datetime:datetime, booking_id:int):
        """!Initialize a Payment object.
        @param payment_id The unique identifier for the payment.
        @param amount The amount of the payment.
        @param payment_datetime The date and time when the payment was made.
        @param booking_id The unique identifier of the booking associated with the payment.
        """
        payment_id = Payment.next_id
        next_id += 1
        pass


class Notification:
    """!The Notification class"""
    next_id = 1
    def __init__(self, send_datetime:datetime, content:str):
        """Initialize the Notification object"""
        self.notification_id = Notification.next_id
        Notification.next_id += 1
        pass

    def send(self):
        """!Send the notification."""
        pass