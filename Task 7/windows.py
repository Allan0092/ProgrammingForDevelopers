from tkinter import *
from tkinter import messagebox
from application_objects import *
from database import DataOperations

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
        self.repository = DataOperations()
    
    def forget_frame(self, *frames: LabelFrame):
        """removes a frame from the screen

        Args:
            frame (LabelFrame): the frame to be removed.
        """
        for frame in frames:
            frame.grid_forget()

    def login_window(self):
        self.login_frame = LabelFrame(self.root, border=10, padx=100, pady=50)
        self.login_frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="W")

        #For getting username
        Label(self.login_frame, text="Username: ").grid(row=1, column=1, padx=(30, 0))
        login_username = Entry(self.login_frame)
        login_username.grid(row=1, column=2, padx=(0, 80))

        def login_button_clicked():
            if login_username.get() == "":
                return
            user = self.repository.find_user(login_username.get())
            if user is not None:
                self.user = user
                self.forget_frame(self.login_frame)
                self.homepage()
            else:
                self.create_an_account_window(login_username.get())


        Button(self.login_frame, text="login", background="GREEN", command=login_button_clicked).grid(row=2, column=1, columnspan=2, pady=(20, 0))

    def create_an_account_window(self, username):
        self.forget_frame(self.login_frame) # remove login frame
        create_an_account_frame = LabelFrame(self.root, border=10, padx=100, pady=50) # create a new frame

        def ok_button_clicked():
            self.user = User(username)
            self.repository.store_user(self.user)
            self.forget_frame(create_an_account_frame)
            self.homepage()

        def back_button_clicked():
            self.forget_frame(create_an_account_frame)
            self.login_window()
        
        label1 = Label(create_an_account_frame, text="Account Not Found")
        label1.grid(row=0, column=0, columnspan=2)
        label2 = Label(create_an_account_frame, text="Create a new Account?")
        label2.grid(row=1, column=0, columnspan=2)
        Button(create_an_account_frame, text="OK", command=ok_button_clicked).grid(row=2, column=0)
        Button(create_an_account_frame, text="Back", command=back_button_clicked).grid(row=2, column=1)
        create_an_account_frame.grid(row=0, column=0)


    def homepage(self):
        welcome_label = Label(self.root, text=f"Hello {self.user.username}")
        welcome_label.grid(row=0, column=0)

    def handle_login(self, username: str):
        self.loggedIn = True
        self.user = User(username)