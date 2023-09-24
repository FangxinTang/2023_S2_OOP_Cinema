from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, fname: str, lname: str, username: str, password: str):
        self._fname = fname
        self._lname = lname
        self._username = username
        self._password = password

    # Getters and Setters
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
        self._password = new_password

    # Abstract Method
    @abstractmethod
    def info(self):
        pass
