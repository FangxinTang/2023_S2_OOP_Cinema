from a_models import *
from b_controller import *
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "123456789"

################## Create objects ######################
#### 1. controller
my_controller = Controller()


### 2. cinema
with open('src/db/cinema.txt', 'r') as file:
    info = file.readline().split('|')
    cinema_params = (info[0], int(info[1]), int(info[2]), info[3])
    lincoln_cinema = my_controller.create_cinema(*cinema_params)
    my_controller.add_cinema(lincoln_cinema)
# print(lincoln_cinema)


### 3. hall and seats
with open("src/db/cinema_hall.txt", 'r') as file:
    lines = file.readlines()
    for line_num, line in enumerate(lines):
        line = line.strip().split('|')
        hall_params = (line[0], int(line[1]))
        hall_obj = CinemaHall(*hall_params)
        
        with open(f'src/db/hall_{line_num+1}_seats_data.txt','r') as file:
            hall_seats_lines =file.readlines()
            for line in hall_seats_lines:
                line = line.strip().split('|')
                seats_params = (line[0],float(line[1]),eval(line[2]))
                seat_obj = HallSeat(*seats_params)
                hall_obj.add_seat(seat_obj) # add the seat to the hall
        my_controller.add_hall(hall_obj) # add the hall to the controller

# Access the created halls and their seats 
# for hall in my_controller.halls:
#     print(hall)
#     print("-----------------------")
#     for seat in hall.seats:
#         print(f"  {seat}")


### 4. screening
with open('src/db/screenings.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        info = line.strip().split('|')
        screening_params = (
            info[0], # movie title
            int(info[1]), # hall id
            datetime.strptime(info[2],'%Y-%m-%d').date(),# date
            datetime.strptime(info[3],'%H:%M:%S').time(), #start time
            datetime.strptime(info[4],'%H:%M:%S').time() # end time
        )
        # print(screening_params)
        screening = Screening(*screening_params)
        # print(screening)
        my_controller.screenings.append(screening)
# print(my_controller.screenings)


### 5. movie
with open('src/db/movie.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        info = line.strip().split('|')
        movie_params = (info[0],#title
                        info[1],#description
                        int(info[2]),#duration
                        info[3],#language
                        info[4],#country
                        info[5],#genre
                        info[6])#release date)
        new_movie = Movie(*movie_params) 

        # get all screenings from controller
        all_screenings = my_controller.screenings
        # assign screening to movie
        for screening in all_screenings:
            if screening.movie_title == new_movie.title:
                my_controller.assign_screening_to_movie(screening, new_movie)
        # print(new_movie)

        if new_movie not in my_controller.movies:
            my_controller.add_movie(new_movie)
# print(my_controller.movies[0].screenings[0])
# print(my_controller.movies[0].screenings)


### 6. Customer
with open('src/db/customers.txt') as file:
    lines = file.readlines()
    for line in lines:
        info = line.strip().split('|')
        # print(info)
        customer_params = (info[0],info[1],info[2],info[3])
        new_customer = my_controller.create_customer(*customer_params)
        if new_customer not in my_controller.customers:
            my_controller.customers.append(new_customer)
            if new_customer not in my_controller.users:
                my_controller.users.append(new_customer)
# print(my_controller.customers[0].info())


### 7. Staff
with open('src/db/staff.txt') as file:
    lines = file.readlines()
    for line in lines:
        info = line.strip().split('|')
        # print(info)
        staff_params = (info[0],info[1],info[2],info[3],info[4])
        new_staff = my_controller.create_staff(*staff_params)
        if new_staff not in my_controller.staff:
            my_controller.staff.append(new_staff)
            if new_staff not in my_controller.users:
                my_controller.users.append(new_staff)
# print(my_controller.users)
# print()
# print(my_controller.staff)


### 8. Receptionist and Admin
my_controller.add_front_to_receptionists()
my_controller.add_admin_to_admins()
# print(my_controller.receptionists)
# print(my_controller.admins)


### 9. Booking
with open('src/db/booking.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        info = line.strip().split('|')
        booking_params = (
            int(info[0]),#user_id
            int(info[1]),#screening_id
            int(info[2]),#num_seats
            datetime.strptime(info[3],'%Y-%m-%d %H:%M:%S'),#booking_date
            int(info[4]))#payment_id
        new_booking = my_controller.create_booking(*booking_params)
        if new_booking not in my_controller.bookings:
            my_controller.bookings.append(new_booking)
# print(my_controller.bookings[0])
        # add new booking to customer's bookings list
        wanted_username = my_controller.find_username_by_user_id(new_booking.user_id)
        # check who made the booking, customer or front desk
        selected_customer = my_controller.find_customer_by_username(wanted_username)
        if selected_customer is not None:
            selected_customer.customer_bookings.append(new_booking)
            # print(selected_customer.customer_bookings[0])
        else: 
            print("front staff made the booking")


### 10. Payment
with open('src/db/payment.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        info = line.strip().split('|')
        payment_params = (float(info[0]), datetime.strptime(info[1],'%Y-%m-%d %H:%M:%S'), int(info[2]))
        # print(payment_params)
        payment = my_controller.create_payment(*payment_params)
# print(payment)

### 11. Notification







######################################## View ##############################

@app.route("/")
def home():
    movie_list = my_controller.movies  # data for display the movie list

    language_list = my_controller.get_all_movie_language_list() # data for search function - drop down menu. return a list of string 
    genre_list = my_controller.get_all_movie_genre_list() # data for search function
    date_list = my_controller.get_all_release_date_list() # data for search function


    return render_template('home.html',
                           movie_list=movie_list,
                           language_list=language_list,
                           genre_list=genre_list,
                           date_list=date_list
                           )

# @app.route("/login", methods = ["POST"])
# def login():
#     input_username = request.form.get('username')
#     input_password = request.form.get('password')
#     if my_controller.login(input_username, input_password):
#         my_controller.check_user_role():

@app.route("/search-movie", methods=["GET","POST"])
def search_movie():
    if request.method == "POST":
        title = request.form.get("title")
        language = request.form.get("language")
        genre = request.form.get("genre")
        release_date = request.form.get("release_date")

        filtered_movies = my_controller.search_movies(title, language, genre, release_date)
        return render_template("filtered_movies.html", movies=filtered_movies)

    return redirect("/")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        input_username = request.form.get('username')
        input_password = request.form.get('password')
        print(input_username)
        print(input_password)

        all_users = my_controller.get_all_usernames()

        if my_controller.check_username_pw_match(input_username, input_password):
            session['username'] = input_username

            role = my_controller.check_user_role(input_username)
            if role == 2:
                flash("Welcome back, Customer","success")
                return redirect(url_for('customer_dashboard'))
            elif role == 1:
                flash("Welcome back, Admin","success")
                return redirect(url_for('admin_dashboard'))
            else:
                flash("Welcome back, Receptionist","success")
                return redirect(url_for('receptionist_dashboard'))
            
        else:
            if not my_controller.input_username_is_exist(input_username):
                flash("Username not found.", "warning")
                return redirect("/")
            else:
                flash("Wrong Password. Please Try again", "warning")
                return redirect("/")
    return render_template("home.html")

@app.route("/customer-dashboard")
def customer_dashboard():
    return render_template("customer_dash.html")

@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin_dash.html")

@app.route("/receptionist-dashboard")
def receptionist_dashboard():
    return render_template("receptionist_dash.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
