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
    

    ############# Methods #############  
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
    
    def create_booking(self, user_id, screening_id, num_seats, booking_datetime, payment_id, booked_seats):
        booking = Booking(user_id, screening_id, num_seats, booking_datetime, payment_id, booked_seats)
        return booking
    
    def create_payment(self,amount, payment_datetime, booking_id):
        payment = Payment(amount, payment_datetime, booking_id)
        return payment

    def create_notification(self, send_datetime: datetime, content: str, payment_id:int):
        notification = Notification(send_datetime, content,payment_id)
        return notification

    #############################

    def add_cinema(self, cinema_obj):
        if cinema_obj not in self.cinemas:
            self.cinemas.append(cinema_obj)

    def add_hall(self, hall_obj):
        if hall_obj not in self.halls:
            self.halls.append(hall_obj)

    def add_new_customer_to_db(self, new_customer):
        self.customers.append(new_customer)
        self.users.append(new_customer)

    def add_movie(self, movie_obj):
        self.movies.append(movie_obj)
    
    def assign_screening_to_movie(self,screening, movie):
        movie.add_screening(screening)

    def add_front_to_receptionists(self):
        for staff in self.staff:
            if staff.role == "0" and staff not in self.receptionists:
                self.receptionists.append(staff)

    def add_admin_to_admins(self):
        for staff in self.staff:
            if staff.role == "1" and staff not in self.admins:
                self.admins.append(staff)

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

    ################ search movies ###################
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
    
    def get_user_id_by_username(self, username):
        for user in self.users:
            if user.username == username:
                user_id = user.user_id
        return user_id
    
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


    ############################ customer - booking #########################
            
    def get_hall_obj_by_hall_id(self, hall_id):
        for hall in self.halls:
            if int(hall.hall_id) == int(hall_id):
                return hall
        return None
    
    def get_remaining_available_seats_in_hall(self,hall_id):#list
        hall = self.get_hall_obj_by_hall_id(hall_id)
        return hall.get_remaining_available_seats()
    
    def get_num_remaining_available_seats_in_hall(self, hall_id):
        hall = self.get_hall_obj_by_hall_id(hall_id)
        return hall.get_num_of_seats_available()#int
    
    def get_num_remaining_available_VIP_seats(self, hall_id):
        hall = self.get_hall_obj_by_hall_id(hall_id)
        available_VIP_seats = []
        for seat in hall.seats:
            if seat.seat_type == "VIP" and seat.is_available is True:
                available_VIP_seats.append(seat)
        return len(available_VIP_seats)
    
    def get_num_remaining_available_regular_seats(self, hall_id):
        hall = self.get_hall_obj_by_hall_id(hall_id)
        available_regular_seats = []
        for seat in hall.seats:
            if seat.seat_type == "Regular" and seat.is_available is True:
                available_regular_seats.append(seat)
        return len(available_regular_seats)
    
    def get_num_remaining_available_accessible_seats(self, hall_id):
        hall = self.get_hall_obj_by_hall_id(hall_id)
        available_accessible_seats = []
        for seat in hall.seats:
            if seat.seat_type == "Accessible" and seat.is_available is True:
                available_accessible_seats.append(seat)
        return len(available_accessible_seats)
    
    def add_new_bookings_to_all_bookings(self,new_booking):
        if new_booking not in self.bookings:
            self.bookings.append(new_booking)
    
    def add_new_payment_to_all_payments(self, new_payment):
        if new_payment not in self.payments:
            self.payments.append(new_payment)
    
    def add_payment_id_to_booking(self,booking_id,payment_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.add_payment_id(payment_id)

    def add_notification_to_booking(self, booking_id, notification):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.notification = notification

    def customer_book_seats(self, hall_id, num_vip, num_reg, num_acc, booking_obj, customer_obj):
        for hall in self.halls:
            if hall.hall_id == hall_id:

                booked_seats = []

                for seat in hall.seats:
                    if seat.seat_type == "VIP" and num_vip > 0 and seat.is_available:
                        seat.is_available = False
                        booked_seats.append(seat)
                        num_vip -= 1
                        # print("Add vip", booked_seats)
                    elif seat.seat_type == "Regular" and num_reg > 0 and seat.is_available:
                        seat.is_available = False
                        booked_seats.append(seat)
                        num_reg -= 1
                        # print("Add reg", booked_seats)
                    elif seat.seat_type == "Accessible" and num_acc > 0 and seat.is_available:
                        seat.is_available = False
                        booked_seats.append(seat)
                        num_acc -= 1
                        # print("Add ac", booked_seats)
                print("cusomter_book_seats: Booked_seats: ", booked_seats)

                # # add the booked_seats to the booking_obj
                # booking_obj.booked_seats.extend(booked_seats)
                # print(booking_obj.booked_seats)

                # add the booking obj to customer bookings if not already exist
                if booking_obj not in customer_obj.customer_bookings:
                    customer_obj.customer_bookings.append(booking_obj)
                    print(customer_obj.customer_bookings)

                # update the overall bookings in the booking system  
                if booking_obj not in self.bookings:  
                    self.bookings.append(booking_obj)
    
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

############################ customer cancel booking #########################

    def get_booking_obj_by_booking_id(self,booking_id):
        for booking_obj in self.bookings:
            if int(booking_obj.booking_id) == int(booking_id):
                return booking_obj
            
    def get_payment_id_by_booking_id(self, booking_id):
        for payment in self.payments:
            if int(payment.paymeng_id) == int(booking_id):
                return int(payment.payment_id)
            
    def remove_a_booking(self,booking_obj):
        if booking_obj in self.bookings:
            self.bookings.remove(booking_obj)
            return "booking has been canceled"
        else:
            return "booking not exist"
        
############################ front desk book tickets #########################
    def get_screening_by_screening_id(self, screening_id):
        for s in self.screenings:
            if int(s.screening_id) == int(screening_id):
                return s

        
############################# admin ########################
    def add_new_movie(self,new_movie):
        if new_movie not in self.movies:
            self.movies.append(new_movie)
        else:
            return "This movie already exist"
    
    def remove_movie(self,movie):
        if movie in self.movies:
            self.movies.remove(movie)
        else:
            return "This movie already exist"

    def add_screening(self, screening:Screening):
        if screening not in self.screenings:
            self.screenings.append(screening)
        else:
            return "The screening already exist"

    def cancel_screening(self, screening:Screening):
        if screening in self.screenings:
            self.screenings.remove(screening)


