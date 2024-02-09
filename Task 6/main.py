import asyncio
import tkinter as tk
import webscrape as WS




def main_window():

    root = tk.Tk()
    root.title("Text Box Inputs")

    # Create and place labels and text boxes
    label1 = tk.Label(root, text="Input 1:")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(root, text="Input 2:")
    label2.grid(row=1, column=0)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    label3 = tk.Label(root, text="Input 3:")
    label3.grid(row=2, column=0)
    entry3 = tk.Entry(root)
    entry3.grid(row=2, column=1)

    def retrieve_input():
        input1 = entry1.get()
        input2 = entry2.get()
        input3 = entry3.get()
        print("Input 1:", input1)
        print("Input 2:", input2)
        print("Input 3:", input3)
        # Create and place the button
    
    button = tk.Button(root, text="Retrieve Input", command=retrieve_input)
    button.grid(row=3, columnspan=2)

    # Run the Tkinter event loop
    root.mainloop()


def main():
    urls = ["https://www.yetitrailadventure.com/", "https://www.anepaltrek.com/activities-category/annapurna-trekking/", "https://www.lonelyplanet.com/nepal"]
    WS.getData("https://www.lonelyplanet.com/nepal")

if __name__ == "__main__":
    main()