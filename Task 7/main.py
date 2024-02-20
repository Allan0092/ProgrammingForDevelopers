from tkinter import *

from windows import Window


def main():
    win = Window(Tk())
    win.login_window()
    win.root.mainloop()


if __name__ == "__main__":
    main()