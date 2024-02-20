from tkinter import Tk

from windows import Window


def main():
    window = Window(Tk())
    window.window()
    window.root.mainloop()

if __name__ == "__main__":
    main()