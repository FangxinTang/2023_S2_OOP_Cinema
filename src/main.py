from a_models import *
from b_controller import *
import os

print("Current working direcotry: ", os.getcwd())
print("------------")

############# Create Controller Object #############
my_controller = Controller()

################## Functions #######################
def parse_screening_line(line):
    hall_id, screening_date_str, start_time_str, end_time_str = line.strip().split("|")
    screening_date = datetime.strptime(screening_date_str, "%Y-%m-%d")
    start_time = datetime.strptime(start_time_str, "%H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%H:%M:%S")
    return Screening(hall_id=int(hall_id), screening_date=screening_date, start_time=start_time, end_time=end_time)


##################### Create Objects ###############
# 1. Cinema
with open("src/db/cinema.txt", 'r') as file:
    cinema_data = file.readline().strip().split("|")
    print("cinema_data before = ", cinema_data)
    print()

    # format the data
    cinema_name = cinema_data[0]
    total_halls = int(cinema_data[1])
    total_seats = int(cinema_data[2])
    location = cinema_data[3]

    # pass data into controller
    cinema = my_controller.create_cinema(cinema_name, total_halls, total_seats, location)
    print(cinema)



# 2. CinemaHall
with open("src/db/cinema_hall.txt", 'r') as file:
    hall_data_lines = file.readlines()

    # get each hall's capacity
    for line_number, line in enumerate(hall_data_lines, start=1):
        capacity = int(line.strip())
        print(f"--------line number/hall id:{line_number}, capacity = {capacity}")
        
        # within each hall, open it's seat data
        with open(f"src/db/hall_{line_number}_seats_data.txt", 'r') as file:
            seat_data_lines =file.readlines()
            # print(seat_data_lines) 

            # create each cinema hall inside the loop
            my_cinema_hall = my_controller.create_cinema_hall(capacity=capacity,seat_data_lines=seat_data_lines)
            # print(my_cinema_hall)
            # print("~~~~~~~~~~~~~~~~~~~~~")

        # Store the cinema hall instance in the dictionary with hall_id as key
        # cinema_halls[f"hall_{line_number}"] = my_cinema_hall
# print(cinema_halls["hall_1"])
# Print information for each CinemaHall instance in the dictionary
# for hall_id, cinema_hall in cinema_halls.items():
#     print(f"Information for {hall_id}:")
#     print(cinema_hall)
#     print("~~~~~~~~~~~~~~~~~~~~~")


# # 3. Movie with Screenings
# with open("src/db/movie.txt",'r') as file:
#     movie_lines = file.readlines()

#     for line_number, line in enumerate(movie_lines, start=1): 
#         movie_data = line.strip().split("|")
#         "title": movie_data[0]
#         "description": movie_data[1]
#         "duration_mins": int(movie_data[2])
#         "language": movie_data[3]
#         "release_date": datetime.strptime(movie_data[4], "%Y,%m,%d"),
#         "country": movie_data[5]
#         "genre": movie_data[6]

#         with open(f"src/db/movie_{line_number}_screenings.txt")



