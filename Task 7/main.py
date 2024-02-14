from tkinter import *

from windows import window


def main():
    win = window(Tk())
    win.login_window()
    win.root.mainloop()


if __name__ == "__main__":
    main()