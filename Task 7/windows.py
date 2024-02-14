from tkinter import *
from tkinter import messagebox
from application_objects import *

class window:
    def __init__(self, root: Tk):
        self.root = root
        self.height = 800
        self.width = 800
        self.root.minsize(self.height, self.width)
        self.root.title("Tiktok")
        self.login_frame = None
        self.header = None
        self.loggedIn = False
        self.user: User = None
    
    def forget_frame(self, *frames: LabelFrame):
        """removes a frame from the screen

        Args:
            frame (LabelFrame): the frame to be removed.
        """
        for frame in frames:
            frame.grid_forget()

    def login_window(self):
        self.login_frame = LabelFrame(self.root, border=10, padx=100, pady=100)
        self.login_frame.grid(row=1, column=1)

        #For getting username
        Label(self.login_frame, text="Username: ").grid(row=1, column=1, padx=30)
        login_username = Entry(self.login_frame)
        login_username.grid(row=1, column=2, padx=(0, 80))

        Button(self.login_frame, text="login", background="GREEN").grid(row=2, column=1, columnspan=2)

    def handle_login(self, username: str):
        self.loggedIn = True
        self.user = User(username)