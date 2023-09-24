from user import *

class Customer(User):  
    def __init__(self, fname: str, lname: str, username: str, password: str):
        super().__init__(fname, lname, username, password)
        self._bookings = []

    # Getter for bookings
    @property
    def bookings(self):
        return self._bookings

    # Setter for bookings
    @bookings.setter
    def bookings(self, new_bookings):
        self._bookings = new_bookings

    

    def info(self):
        full_name = self.full_name()
        info_text = f"Customer Info:\nFull Name: {full_name}\nUsername: {self.username}\n"
        if self.bookings:
            bookings_str = ", ".join(self.bookings)
            info_text += f"Bookings: {bookings_str}"
        else:
            info_text += "Bookings: No booking is found."


    
