from a_models import *
from b_controller import *
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "123456789"

################ Constants ##################
TICKET_PRICES = {
    "VIP": 20.0,
    "Regular": 10.0,
    "Accessible": 15.0
}

NOTIFICATION_CONTENT ={
    "Booked" : "You have booked the tickets. Enjoy the movie.",
    "Cancelled" :"You have cancelled the tickets. See you next time"
}


################################## Creating Objects ##############################
#### 1. Controller
my_controller = Controller()


### 2. Cinema
with open('src/db/cinema.txt', 'r') as file:
    info = file.readline().split('|')
    cinema_params = (info[0], int(info[1]), int(info[2]), info[3])
    lincoln_cinema = my_controller.create_cinema(*cinema_params)
    my_controller.add_cinema(lincoln_cinema)


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
        screening = Screening(*screening_params)
        my_controller.screenings.append(screening)


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
            int(info[4]),#payment id 
            eval(info[5]))#booked seat
        new_booking = my_controller.create_booking(*booking_params)
        if new_booking not in my_controller.bookings:
            my_controller.bookings.append(new_booking)
        print(my_controller.bookings[0])
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


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        fname=request.form.get("fname").capitalize()
        lname=request.form.get('lname').capitalize()
        username=request.form.get('username')
        password=request.form.get('password')

        # Server-side validation
        if not fname or not lname or not username or not password:
            flash("Please fill out all required fields.", "warning")
            return redirect(url_for('register'))  

        # Check if username already exists
        existing_usernames = my_controller.get_all_usernames()
        if username in existing_usernames:
            flash("Username already exists. Please choose another.", "warning")
            return redirect(url_for('register'))  
        
        # if all good, create new customer object, add customer into list
        new_customer = my_controller.create_customer(fname, lname, username, password)
        my_controller.add_new_customer_to_db(new_customer)
        flash("You have registered. You can login now.", "success")
        return redirect(url_for('home'))

    return render_template("/register.html")


@app.route("/customer-dashboard")
def customer_dashboard():
    movie_list = my_controller.movies  # data for display the movie list

    language_list = my_controller.get_all_movie_language_list() # data for search function - drop down menu. return a list of string 
    genre_list = my_controller.get_all_movie_genre_list() # data for search function
    date_list = my_controller.get_all_release_date_list() # data for search function

    return render_template("customer_dash.html",
                           movie_list=movie_list,
                           language_list=language_list,
                           genre_list=genre_list,
                           date_list=date_list)

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

################################### booking and pay ###########################
@app.route("/booking/<int:screening_id>", methods=["POST","GET"])
def booking(screening_id):

    print("screening_id", screening_id, type(screening_id))

    if "username" not in session:
        flash("Please log in to book.", "warning")
        return redirect(url_for('home'))
    else:
        role = my_controller.check_user_role(session["username"])
        if role == 1:
            flash("You are not authorized to book tickets", "warning")
            return redirect(url_for('admin_dashboard'))
        
        else:
            for screening in my_controller.screenings:
                if int(screening.screening_id) == int(screening_id):
                    selected_screening = screening
                    selected_hall_id = int(screening.hall_id)
            print("selected_hall_id: ", selected_hall_id, type(selected_hall_id))

            hall = my_controller.get_hall_obj_by_hall_id(selected_hall_id)
            if hall is not None:
                remaining_available_seats_in_hall = my_controller.get_remaining_available_seats_in_hall(selected_hall_id)
                num_remaining_available_seats_in_hall = my_controller.get_num_remaining_available_seats_in_hall(selected_hall_id)
                num_remaining_available_VIP_seats = my_controller.get_num_remaining_available_VIP_seats(selected_hall_id)
                num_remaining_available_regular_seats = my_controller.get_num_remaining_available_regular_seats(selected_hall_id)
                num_remaining_available_accessible_seats = my_controller.get_num_remaining_available_accessible_seats(selected_hall_id)

                username = session['username']
                user_id = my_controller.get_user_id_by_username(username)
                booking_datetime = datetime.now()

                
                return render_template("booking.html", 
                                    screening_id=screening_id, 
                                    screening=selected_screening,
                                    hall=hall,
                                    remaining_seats=remaining_available_seats_in_hall,
                                    num_remaining_seats=num_remaining_available_seats_in_hall,
                                    num_vip = num_remaining_available_VIP_seats,
                                    num_regular = num_remaining_available_regular_seats,
                                    num_accessible = num_remaining_available_accessible_seats,
                                    ticket_prices = TICKET_PRICES,
                                    user_id=user_id,
                                    booking_datetime=booking_datetime)
            else:
                flash("hall not found", "warning")
                return render_template('customer_dash.html')

@app.route("/booking-details", methods=["GET", "POST"])
def booking_details():
    if request.method == "POST":

        user_id=int(request.form.get("user_id"))
        screening_id=int(request.form.get("screening_id"))#str
        booking_datetime=request.form.get("booking_datetime")
        # Print values to the console for debugging
        print("User ID:", user_id, "Type:", type(user_id))
        print("Screening ID:", screening_id, "Type:", type(screening_id))
        print("Booking Datetime:", booking_datetime, "Type:", type(booking_datetime))


        n_vip = request.form.get("vip")
        n_reg = request.form.get("regular")
        n_acc = request.form.get("accessible")

        # Handle the case where the form value is not provided or is an empty string
        n_vip = int(n_vip) if n_vip and n_vip.isdigit() else 0
        n_reg = int(n_reg) if n_reg and n_reg.isdigit() else 0
        n_acc = int(n_acc) if n_acc and n_acc.isdigit() else 0
        # Print values to the console for debugging
        print("Number of VIP tickets:", n_vip)
        print("Number of Regular tickets:", n_reg)
        print("Number of Accessible tickets:", n_acc)
    
        num_seats = n_vip+n_reg+n_acc
        print(num_seats)
        total_amount = n_vip * TICKET_PRICES["VIP"] + n_reg * TICKET_PRICES["Regular"]+n_acc*TICKET_PRICES["Accessible"]
        print(total_amount)

        # #get screening_obj
        # all_screenings = my_controller.screenings
        # print(all_screenings[0])
        # for screening in all_screenings:
        #     if screening.screening_id == int(screening_id):
        #         print("yes")
        #     else:
        #         print("no")

        for screening in my_controller.screenings:
            if screening.screening_id == screening_id:
                screening_obj=screening
        print(screening_obj )

        username=session["username"]
        print("Username: ", username)

        return render_template("booking_details.html",
                        user_id=user_id,
                        username=username,
                        screening_id=screening_id,
                        screening_obj=screening_obj,
                        vip=n_vip,
                        regular=n_reg,
                        accessible=n_acc,
                        num_seats=num_seats,
                        booking_datetime=booking_datetime,
                        total_amount=total_amount)

    # Handle the case when the request method is GET (render a different template or redirect if needed)
    return render_template("booking_details.html")

@app.route('/confirm-booking', methods=["POST"])
def confirm_booking():
    """
    this route to change the seat availability in HallSeat according to user input,
    create a new booking object, add add new booking to all booking list,
    add the new booking object to customer.customer_bookings
    create a new payment, which is associate with a booking id
    create new notification, which is associate with a payment id
    """
    # Retrieve form data from the POST request   
    vip_tickets = int(request.form.get('vip'))
    regular_tickets = int(request.form.get('regular'))
    accessible_tickets = int(request.form.get('accessible'))
    total_amount = float(request.form.get('total_amount'))
    hall_id = request.form.get("hall_id")
    if hall_id:
        hall_id=int(hall_id)
    else:
        print("error:hall id is emplty")
    # for creating new booking
    user_id = int(request.form.get('user_id'))
    screening_id = int(request.form.get('screening_id'))
    num_seats = int(request.form.get('num_seats'))
    booking_datetime = request.form.get('booking_datetime') #str


    # check bugs
    print("vip_tickets:", vip_tickets, type(vip_tickets))
    print("regular_tickets:", regular_tickets, type(regular_tickets))
    print("accessible_tickets:", accessible_tickets, type(accessible_tickets))
    print("total_amount:", total_amount, type(total_amount))
    print("hall_id:", hall_id, type(hall_id))
    print("user_id:", user_id, type(user_id))
    print("screening_id:", screening_id, type(screening_id))
    print("num_seats:", num_seats, type(num_seats))
    print("booking_datetime:", booking_datetime, type(booking_datetime))

    # create new booking - to add payment_id, and booked_seats later
    new_booking = my_controller.create_booking(user_id,screening_id,num_seats,booking_datetime,payment_id=None, booked_seats=None)
    print("inital booking - no payment id, no booked seat", new_booking)
    print("`~~~~~~~~~~~~~~")

    # get customer
    username = session["username"]
    customer_obj = my_controller.find_customer_by_username(username)
    print(customer_obj)
    
    # customer_book_seats
    ### update - seat availability in HallSeats 
    ### add - booked seats in booking
    for hall in my_controller.halls:
        if hall.hall_id == hall_id:
            booked_seats = []
            for seat in hall.seats:
                for seat in hall.seats:
                    if seat.seat_type == "VIP" and vip_tickets > 0 and seat.is_available:
                        seat.is_available = False
                        booked_seats.append(seat)
                        vip_tickets -= 1
                        print("Add vip", booked_seats)

                    elif seat.seat_type == "Regular" and regular_tickets > 0 and seat.is_available:
                        seat.is_available = False
                        booked_seats.append(seat)
                        regular_tickets -= 1
                        print("Add reg", booked_seats)

                    elif seat.seat_type == "Accessible" and accessible_tickets > 0 and seat.is_available:
                        seat.is_available = False
                        booked_seats.append(seat)
                        accessible_tickets -= 1
            print("all seats booked: ", booked_seats)
            # add this booked_seats list to booking's booked_seats
            new_booking.booked_seats = booked_seats
            print(" booking's booked seats: ",new_booking.booked_seats)
            print(">>>>>>>>>>>>")


    # create new payment - to add notification later
    payment_datetime = datetime.now()
    booking_id = new_booking.booking_id
    new_payment = my_controller.create_payment(total_amount, payment_datetime,booking_id)
    print("New Payment: ", new_payment)
    print("<<<<<<<<<<<<<<<<<<<<<<")

    ## add payment_id to new booking
    payment_id = new_payment.payment_id
    my_controller.add_payment_id_to_booking(booking_id,payment_id)
    print("New Booking final: ", new_booking)
    print(">>>>>>>>>>>>>>>>>>>>>>>>")

    ### update - add this new booking into controller bookings
    my_controller.bookings.append(new_booking)
    print("all bookings - ", my_controller.bookings[0])
    print("..............")

    ### update - customer - customer bookings
    customer_obj.customer_bookings.append(new_booking)
    print("Customer obj: ", customer_obj.info())

    # create new notification
    send_datetime = datetime.now()
    content = NOTIFICATION_CONTENT["Booked"]
    new_notification = my_controller.create_notification(send_datetime, content,payment_id)
    

    # flash("all good", "success")
    # print("New booking: ", new_booking.booked_seats)
    return render_template('confirm_booking.html',
                           note=new_notification,
                           customer=customer_obj,
                           payment=new_payment,
                           booking=new_booking
                           )

@app.route("/cancel-booking/<booking_id>")
def cancel_booking(booking_id):
    """
    1-remove booking from all booking list
    2-release seat is available to True
    3-remove booking from customer's booking list
    4-no refund :)
    5-send notification
    """
    #1 remove booking from all booking list
    ## get booking by booking id
    cancel_notification = None

    for customer in my_controller.customers:
        if customer.username == session["username"]:
            break  

    for booking in my_controller.bookings:
        if booking.booking_id == booking_id:
            print("before seat avai", booking.booked_seats)
            seats_to_release = list(booking.booked_seats)

            for seat in seats_to_release:
                seat.is_available = True  # Release seat
                print("after seat avai", booking.booked_seats)

            customer.customer_bookings.remove(booking)

    print("customer booking after", customer.customer_bookings)
    print("cancel notification: ", cancel_notification)
    print("after remove all booking list", len(my_controller.bookings))
    flash("You booking has been canceled","success")
    return render_template("cancel_booking_result.html")

@app.route("/screening-list")
def screening_list():
    screenings = my_controller.screenings
    return render_template("screening_list.html",screenings=screenings)

@app.route("/handle-front-book/<screening_id>")
def handle_front_book(screening_id):
    """
    similar to customer booking
    """
    # get screening by secreen id
    # get hall id by screening
    # get hall by hall id
    # get hall seats list 
    # get each seat type's number of available seats 
    # send to template to render
    pass

@app.route("/front-confirm-booking")
def front_confirm_booking():
    """
    similar to cusotmer booking
    """
    # get data from the templete

    # create a new booking object with the data
    # update - seat availability in HallSeats 
    # create - new payment
    # add new booking to controller's booking list

@app.route("/front-cancel")
def front_cancel():
    """
    similar to customer cancel booking"""
    # get booking object
    # get customer object
    # get customer's booming list
    # change the seat object availablity attribute to True again, then release/remove from the list
    # remove the booking object from controller's all booking 
    pass



if __name__ == '__main__':
    app.run(debug=True)
