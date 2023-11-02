import tkinter as tk
from tkinter import ttk, scrolledtext
from tkcalendar import *
import os
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo,showerror
from datetime import date, datetime, timedelta
from a_models import *
from b_controller import *

############# Create Controller Object #############
my_controller = Controller()

############################ Get Data From Files ############################
def load_movie_info_from_file():
    with open('src/db/movie.txt', mode='r') as file:
        movie_lines = file.readlines()
    return movie_lines if movie_lines else None
        
def load_movie_names_from_file():
    movie_names=[]
    with open('src/db/movie.txt', mode='r') as file:
        for line in file:
            line = line.strip().split('|')
            name=line[0]
            movie_names.append(name)
    return movie_names


############################ Btn Functions ############################
def btn_show_movie_list():
    movie_names = load_movie_names_from_file()
    # Clear the previous content in the movie_listbox
    movie_listbox.delete(0, tk.END)
    # populate data into listbox
    for name in movie_names:
        movie_listbox.insert(tk.END, name)
    print("clicked")

############################ Click Functions ############################

############################ Test ############################

############################ GUI ############################
# Create a root
root = tk.Tk() 
root.title("Movie Ticket Booking System")
root.geometry("920x800+30+30")
root.config(padx=10, pady=10)

############## Heading #################
## Create a cinema logo
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
button = ttk.Button(root,text="Show Movie List",command=btn_show_movie_list)
button.grid(row=3,column=0,sticky='nw',pady=5, padx=(30,0))


###### movie description text_widget #########
# movie description text_widget:
## Create a title label for description text widget
description_title_label = ttk.Label(root,text='Description',font=("Helvetica", 16))
description_title_label.grid(row=1,column=1, sticky='w',pady=5,padx=(50,0))

## create the text widget
text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD,width=15, height=20)
text_widget.grid(row=2, column=1,padx=(25,0),sticky='ew')

## get info to pass to the widget
selected_movie_index = movie_listbox.curselection()
print(selected_movie_index)
print("....")
if selected_movie_index:
    movie_lines = load_movie_info_from_file()
    print(movie_lines)
    print(".....")
    selected_movie_info = movie_lines[selected_movie_index]
    print(selected_movie_info)
    print("....")
    format_selected_movie_info = selected_movie_info.strip().split("|")
    print(format_selected_movie_info)
    print("....")
    ## create a movie object.
    selected_movie = my_controller.create_movie(
        title=format_selected_movie_info[0],
        description=format_selected_movie_info[1],
        duration_mins=int(format_selected_movie_info[2]),
        language=format_selected_movie_info[3],
        country=format_selected_movie_info[4],
        genre=format_selected_movie_info[5],
        release_date=datetime.strptime(format_selected_movie_info[6], '%Y-%m-%d')
    )
    
    if selected_movie is not None:
        text_widget.delete('1.0', tk.END) 
        text_widget.insert(tk.END, selected_movie) 
    else:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "No movie infomation available")
    
else:
    selected_movie_index = None



# ## Create a listbox for displaying doctors
# doctor_listbox = tk.Listbox(root, width=30,height=15,exportselection=0,selectmode=tk.SINGLE)
# doctor_listbox.grid(row=2,column=1, sticky='w',padx=(50, 0)) 

# ## Create a button to read data
# button = ttk.Button(root,text="Show All Doctors",command=btn_show_all_doctors)
# button.grid(row=3,column=1,sticky='nw',pady=5, padx=(50,0))



#exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
exit_button.grid(row=9,column=2,sticky='es',pady=(30,0))
root.mainloop()