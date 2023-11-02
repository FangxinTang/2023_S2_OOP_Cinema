import tkinter as tk
from tkinter import ttk, scrolledtext
from tkcalendar import *
import os
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo,showerror
from datetime import date, datetime, timedelta
from a_models import *

############################ Get Data From Files ############################
def load_movie_names_from_file():
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



############################ Click Btn Functions ############################
def btn_show_movie_list():
    movie_names = load_movie_names_from_file()
    # Clear the previous content in the movie_listbox
    movie_listbox.delete(0, tk.END)
    # populate data into listbox
    for name in movie_names:
        movie_listbox.insert(tk.END, name)

####### GUI #######
# Create a root
root = tk.Tk() 
root.title("Movie Ticket Booking System")
root.geometry("920x800+30+30")
root.config(padx=10, pady=10)


# # Create a clinic logo
image_path = os.path.join(os.getcwd())+'/src/logo.png' ## Specify the full path to the image file
print(f"image_path = {image_path}")
img = Image.open(image_path) ## open the image
new_size = (50,50) # set width and height as a tuples
resized_img = img.resize(new_size) ## resize the image
tk_img = ImageTk.PhotoImage(resized_img) # Converting the Pillow Image object into a PhotoImage object for displaying in tkinter

# Place a heading part: label with the logo and cinema name, place the heading at the top centre of the window
heading_label = ttk.Label(
    root, 
    image=tk_img,
    text="Movie Ticket Booking System", 
    font=("Helvetica", 24, "bold"),
    compound='left',
    )
heading_label.grid(row=0,column=1,pady=10)


############# Section One: movie list, movie details, screenings  #############

###### movie list box #########

## Create a title label
movie_lst_title_label = ttk.Label(root,text='Movie List',font=("Helvetica", 16))
movie_lst_title_label.grid(row=1,column=0, sticky='w',pady=5, padx=(30,0))

# ## Create a listbox for displaying movies
movie_listbox = tk.Listbox(root, width=20,height=15, exportselection=0, selectmode=tk.SINGLE)
movie_listbox.grid(row=2,column=0,padx=(30,0))

## Create a button to show all movies
button = ttk.Button(root,text="Show Movie List",command="btn_show_movie_list")
button.grid(row=3,column=0,sticky='nw',pady=5, padx=(30,0))



# # Doctor list:
# ## Create a title label
# doctor_lst_title_label = ttk.Label(root,text='Doctor List',font=("Helvetica", 16))
# doctor_lst_title_label.grid(row=1,column=1, sticky='w',pady=5,padx=(50,0))

# ## Create a listbox for displaying doctors
# doctor_listbox = tk.Listbox(root, width=30,height=15,exportselection=0,selectmode=tk.SINGLE)
# doctor_listbox.grid(row=2,column=1, sticky='w',padx=(50, 0)) 

# ## Create a button to read data
# button = ttk.Button(root,text="Show All Doctors",command=btn_show_all_doctors)
# button.grid(row=3,column=1,sticky='nw',pady=5, padx=(50,0))




root.mainloop()