"""! @brief Lincoln Cinemas Online Movie Ticket System Controller """

##
# @mainpage Lincoln Cinemas Online Movie Ticket System
#
# @section description_main Description
# This system can facilitate the purchase of movie tickets by our customers. This e-ticketing system will 
# allow customers to browse through the movies currently playing and book seats for screenings, anywhere and anytime. 

# @section notes_main Notes
# Add any special notes here

## 
# @file controller.py
#
# @brief this is the controller 
#
# @section description_cinemas Description
# Implementation for cinemas
# 
# @section notes_cinemas Notes
# Additional notes for cinemas
#
# @section author_cinemas Author
# Created by Fangxin Tang on 26/09/2023

# Imports
from a_models import *


class Controller:
    """! The Controller class
    Defines all the methods for the controller
    """
    def __init__(self):
        """! This is the initializer for Controller"""
        self._users = [] 
        self._movies = []  
        self._screenings = []  
        self._bookings = []  
        self._notifications = []  
        self._payments = []

    @property
    def users(self):
        return self._users
    
    @property
    def movies(self):
        return self._movies
    
    def load_movie_names_from_file(self):
        try:
            with open('src/db/movie.txt', mode='r') as file:
                movie_lines = file.readlines()
                movie_names=[]
                # Create a list of movie name list
                for line in movie_lines:
                    movie_names.append(line[0])
            return movie_names
        except FileNotFoundError:
            print('Movie File not found')

    def create_cinema(self, name:str, total_halls:int, total_seats:int, location:str):
        cinema_object = Cinema(name=name, total_halls=total_halls, total_seats=total_seats, location=location)
        return cinema_object
    
    def create_cinema_hall(self, capacity:int,seat_data_lines:str):
        hall_object = CinemaHall(capacity=capacity, seat_data_lines=seat_data_lines)
        return hall_object
    
    def create_movie(self,title:str, language:str, genre:str, release_date:datetime, screening_date:datetime, start_time:datetime, end_time:datetime):
        movie_object = Movie(title:str, language:str, genre:str, release_date:datetime)
    
    

    def login(self,username:str,password:str)->bool:
        """!User login.
        @param username Username
        @param password Password
        @return True if login is successful, False otherwise"""
        pass


    def logout(self):
        """!User logout"""
        pass

    def check_user_role(self):
        """!Check the role of the currently logged-in user.
        @return User role as 'customer', 'receptionist', or 'admin'"""

    def add_new_movie(self,movie:Movie):
        """!This method check the user role is admin then add a new move"""
        pass

    def add_screening(self, screening:Screening):
        """!Check if the user role is admin then add a screening"""
        pass

    def cancel_screening(self, screening:Screening):
        """!Check if the user role is admin then cancel the screening"""
        pass
    def select_movies_by_multi_criteria(
            self,
            title: Optional[str]=None,
            language: Optional[str]=None, 
            genre: Optional[str]=None,
            release_date: Optional[date]=None
            ) -> List[Movie]:
        """!
        Search/select for movies based on specified criteria.
        @param title (str, optional) The title of the movie to search for
        @param language(str, optional) The language of the movie to search for
        @param genre(str, optional) The genre of the movie to search for
        @param release_date
        @return A list of movie objects that match the search criteria
        """
        pass

    def make_ticket_booking(self, booking:Booking):
        """!Check if the user role is customer or receptionist then make a ticket booking."""
        pass


    def select_seats(self, screening_id:int, selected_seats:List[str]):
        """! 
        This method select_seats to allow customers to select one or more available seats based on their preferred seat location.

        @param screening_id: The unique identifier of the screening.
        @param selected_seats: A list of seat IDs representing the seats selected by the customer.
        @return A confirmation message if seats are successfully selected, or an error message if there are issues.
        @rtype: str
        """

    def createCustomer(self, fname: str, lname: str, username: str, password: str):
        """! Create an instance of Customer
        @param fname The first name
        @param lname The last name
        @param username The user name
        @param password The password
        """
        pass



    def view_movie_schedules(self, selected_movie: Movie) -> List[Screening]:
        """!
        This method view_movie_schedules to view the schedules of a selected movie.
        @param selected_movie The selected Movie object.
        @returns List[Screening]: A list of Screening objects representing the schedules of the selected movie.

        """
        pass
    
    def pay_for_tickets(self, payment):
        """!Pay for movie tickets"""
        pass


    
