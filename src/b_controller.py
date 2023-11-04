from a_models import *

class Controller:
    def __init__(self):
        """! This is the initializer for Controller"""
        self._cinemas = []
        self._users = [] 
        self._customers = []
        self._staff = []
        self._receptionists = []
        self._admins = []
        self._movies = [] 
        self._screenings = [] 
        self._bookings = []  
        self._notifications = []  
        self._payments = []
        self._halls = []

    @property
    def cinemas(self):
        return self._cinemas

    @property
    def users(self):
        return self._users
    
    @property
    def customers(self):
        return self._customers
    
    @property
    def staff(self):
        return self._staff
    
    @property
    def receptionists(self):
        return self._receptionists

    @property
    def admins(self):
        return self._admins

    @property
    def movies(self):
        return self._movies
    
    @property
    def screenings(self):
        return self._screenings

    @property
    def bookings(self):
        return self._bookings
    
    @property
    def notification(self):
        return self._notifications
    
    @property
    def payments(self):
        return self._payments
    
    @property
    def halls(self):
        return self._halls
    
    # Methods
    def add_cinema(self, cinema_obj):
        self.cinemas.append(cinema_obj)

    def add_hall(self, hall_obj):
        self.halls.append(hall_obj)

    def add_movie(self, movie_obj):
        self.movies.append(movie_obj)
    
    def assign_screening_to_movie(self,screening, movie):
        movie.add_screening(screening)
        
    def create_cinema(self, name: str, total_halls: int, total_seats: int, location: str):
        cinema = Cinema(name, total_halls, total_seats, location)
        return cinema
    
    def create_cinema_hall(self,hall_name: str, capacity: int):
        hall = CinemaHall(hall_name, capacity)
        return hall
    
    def creat_hall_seat(self ,seat_type, price, is_available, hall_id):
        seat = HallSeat(seat_type, price, is_available, hall_id)
        return seat
    
    def creat_movie(self, title:str, description:str, duration_mins:int, language:str, country:str, genre:str, release_date:datetime):
        movie = Movie(title=title, description=description, duration_mins=duration_mins, language=language, country=country, genre=genre, release_date=release_date)
        return movie
    
    def create_screening(self,hall_obj, movie_obj, screening_date: datetime, start_time: datetime, end_time: datetime):
        screening = Screening(hall_obj, movie_obj, screening_date, start_time, end_time)
        return screening
    
    def create_customer(self,fname: str, lname: str, username: str, password: str):
        customer = Customer(fname, lname, username, password)
        return customer

    def create_staff(self,role,fname,lname,username,password):
        staff = Staff(role,fname,lname,username,password)
        return staff

    def add_front_to_receptionists(self):
        for staff in self.staff:
            if staff.role == "0" and staff not in self.receptionists:
                self.receptionists.append(staff)

    def add_admin_to_admins(self):
        for staff in self.staff:
            if staff.role == "1" and staff not in self.admins:
                self.admins.append(staff)

    def create_booking(self, user_id, screening_id, num_seats, booking_datetime, payment_id):
        booking = Booking(user_id, screening_id, num_seats, booking_datetime, payment_id)
        return booking
    
    def create_payment(self,amount, payment_datetime, booking_id):
        payment = Payment(amount, payment_datetime, booking_id)
        return payment

    def create_notification():
        pass

    def find_username_by_user_id(self, selected_user_id):
        for user in self.users:
            if user.user_id == selected_user_id:
                wanted_username = user.username
                return wanted_username

    def find_customer_by_username(self, wanted_username):
        for customer in self.customers:
            if customer.username == wanted_username:
                return customer
        else:
            return None
    
    def add_new_booking_to_customer_bookings_list(self, selected_customer, new_booking):
        for customer in self.customers:
            if customer.username == selected_customer.username:
                customer.bookings.append(new_booking)

############################# search movies ###################

    def search_movies(self, input_keyword=None, input_language=None, input_genre=None, input_release_date=None):
        filtered_movies = []

        for movie in self.movies:
            title_match = self.check_title_match(movie.title, input_keyword)
            language_match = self.check_language_match(movie.language, input_language)
            genre_match = self.check_genre_match(movie.genre, input_genre)
            date_match = self.check_date_match(movie.release_date, input_release_date)

            if title_match and language_match and genre_match and date_match:
                filtered_movies.append(movie)
        return filtered_movies

    def check_title_match(self, movie_title, input_keyword):
        return input_keyword is None or input_keyword.lower() in movie_title.lower()

    def check_language_match(self, movie_language, input_language):
        return input_language is None or input_language.lower() == movie_language.lower()

    def check_genre_match(self, movie_genre, input_genre):
        return input_genre is None or input_genre.lower() == movie_genre.lower()
    
    def check_date_match(self, movie_release_date, input_release_date):
        return input_release_date is None or input_release_date.lower() == movie_release_date.lower()

    def get_all_movie_language_list(self):
        language_list = []
        for movie in self.movies:
            if movie.language not in language_list:
                language_list.append(movie.language)
        return language_list
    
    def get_all_movie_genre_list(self) -> List:
        genre_list = []
        for movie in self.movies:
            if movie.genre not in genre_list:
                genre_list.append(movie.genre)
        return genre_list
    
    def get_all_release_date_list(self) -> List:
        date_list = []
        for movie in self.movies:
            if movie.release_date not in date_list:
                date_list.append(movie.release_date)
        return date_list
    

############################ authorization #########################
    def check_username_pw_match(self,input_username:str,input_password:str)->bool:
        """!User login.
        @param username Username
        @param password Password
        @return True if login is successful, False otherwise"""
        for user in self.users:
            if input_username == user.username:
                if input_password == user.password:
                    return True
                else:
                    print("Password is incorrect")
                    return False

        # If the loop completes without finding a matching username
        print("Username not found")
        return False
                
    def get_all_usernames(self):
        all_usernames = []
        for user in self.users:
            all_usernames.append(user.username)
        return all_usernames
    
    def input_username_is_exist(self, input_username):
        if input_username in self.get_all_usernames():
            return True
        else:
            return False
    
    def get_user_pw_by_username(self, input_username):
        for user in self.users:
            if user.username == input_username:
                user_pw = user.password
        return user_pw
    


            

    def logout(self):
        """!User logout"""
        pass

    def check_user_role(self, input_username):
        """Check the role of the currently logged-in user.
        Returns:
            0: Admin
            1: Receptionist
            2: Customer
            -1: Role not found (default)"""
        for customer in self.customers:
            if customer.username == input_username:
                return 2 # customer

        for staff in self.staff:
            if staff.username == input_username:
                if staff.role == "0":
                    return 0 # receptionist
                else:
                    return 1 #admin
        return -1 #Role not found


############################ receptionist / customer - booking #########################
    def add_seat_to_booking_lst(self, booking_obj, seat_obj):
        if seat_obj not in booking_obj.booked_seats:
            booking_obj.booked_seats.append(seat_obj)
            return "Seat has been added to booking list"
        else:
            return "Seat has already in booking list"
    
    def remove_seat_to_booking_lst(self, booking_obj, seat_obj):
        if seat_obj in booking_obj.booked_seats:
            booking_obj.booked_seats.remove(seat_obj)
            return "Seat has been removed."
        else:
            return "Seat not been found."
    
    def calculate_total_amount_for_booking(self, booking_obj):
        total = 0
        for seat in booking_obj.seats:
            total += seat.price
        return total

############################ xxx #########################

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

    def customer_add_booking(self, booking_obj):
        """!Make a booking and add it to the booking list.
        @param booking_details Details of the booking, e.g., movie, screening, seats, payment.
        """
        if booking_obj not in self.bookings:
            self.bookings.append(booking_obj)
            return f"Booking successful! Booking ID: {booking_obj.booking_id}"
        else:
            return f"Invalid booking details"

    def customer_remove_booking(self, booking_obj):
        """!Cancel a booking from the booking list.
        @param booking_id: The unique identifier of the booking to be canceled.
        """
        if booking_obj not in self.bookings:
            self.bookings.remove(booking_obj)
            print(f"Booking ID {booking_obj.booking_id} canceled.")
        else:
            print(f"Booking ID {booking_obj.booking_id} not found.")




################# Admin ######################
    @classmethod
    def admin_add_movie(cls, movie_obj):
        """Add a new movie to the cinema's movie list by an admin.
        Args:
            movie_obj: Details of the movie, e.g., title, genre, release date.
        Returns:
            str: A message indicating whether the movie was added or already exists.
        """
        if movie_obj not in cls.movies:
            cls.movies.append(movie_obj)
            return "Movie added successfully."
        else:
            return "This movie already exists."
        
    @classmethod
    def admin_remove_movie(cls, movie_obj):
        """Cancel a new movie to the cinema's movie list by an admin.
        Args:
            movie_obj: Details of the movie, e.g., title, genre, release date.
        Returns:
            str: A message indicating whether the movie was removed or does not exist.
        """
        if movie_obj in cls.movies:
            cls.movies.remove(movie_obj)
            return "Movie deleted successfully."
        else:
            return "This movie does not exist."

    
