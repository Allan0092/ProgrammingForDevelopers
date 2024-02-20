from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time
from random import randint
from myThread import MyThread
import threading
import concurrent.futures

class Window:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.progress_bar = None
        self.url: str = None
        self.image_urls: list[str] = None
        self.downloaded_images = []
        self.saved_images = []
        self.each_image_download_weight = 0

        self.error_message:str = ""
        self.success_label: Label = None
        self.error_label: Label = None
        self.success_message = ""

        self.pause_event = threading.Event()
        self.cancel_event = threading.Event()

        self.root.minsize(150, 100)
        self.root.title("Image Downloader")
        # self.thread = MyThread(self.download_button_clicked, self.pause_event, self.cancel_event)
        self.thread = threading.Thread(target=self.download_button_clicked)
        self.threads:list[threading.Thread] = []
        
        self.pause_button = Button(self.root, text="pause")
        self.resume_button = Button(self.root, text="resume")
        self.cancel_button = Button(self.root, text="cancel")

    def window(self):
        """Main window
        """
        Label(self.root, text="url: ").grid(row=0, column=0, padx=20)
        self.url_input = Entry(self.root)
        self.url_input.grid(row=0, column=1, ipadx=50, padx=(0, 20), columnspan=2, pady=10)
        Button(self.root, text="download", command=self.start_download_thread).grid(row=1, column=0, columnspan=3)

    def start_download_thread(self, _method=None):
        """start multiple threads without issues where you can't restart a thread

        Args:
            _method (self.method): a method/function
        """
        if _method is None:
            _method = self.download_button_clicked
        self.threads.append(threading.Thread(target=_method))
        self.threads[-1].start()

    def get_image_urls(self):
        """get the image urls from the image tags

        Returns:
            list[str]: a list of image urls where you can download images from.
        """
        try: # sends the get request to the given url  
            html_data = requests.get(self.url) 
        except requests.exceptions.MissingSchema: # Incase given invalid url
            self.error_message = "Invalid url"
            self.display_error()
            # self.thread.cancel()
            return
        if html_data.status_code != 200: # if connection cannot be established
            self.error_message = f"{html_data.status_code} connection failed"
            self.display_error()
            self.thread.cancel()
            return
        soup = BeautifulSoup(html_data.text, 'html.parser') # Parses the html tags
        img_tags = soup.find_all("img") # finds all the img tags
        img_urls = []
        for img_tag in img_tags: # Iterate through img tags
            img_url = urljoin(self.url, img_tag.get("src"))
            img_urls.append(img_url)
        return img_urls
    
    def save_image(self, img_url:str, dir="Images"):
        """Downloads a single Image

        Args:
            img_url (str, optional): url of the image. Defaults to "".
            dir (str, optional): the directoty to save the image. Defaults to "Images".

        Returns:
            str: time took to download
        """
        start = time.perf_counter()
        os.makedirs(dir, exist_ok=True) # Create output directory if it doesn't exist
        img_name = img_url.split("/")[-1] # discards the url to get only the image name
        # Download image
        img_data = requests.get(img_url) # Request for image
        try: # when the image name can be extracted easily
            img_file = open(os.path.join(dir, img_name), "wb")
            img_file.write(img_data.content)
            print(f"Image '{img_name}' downloaded.")
            self.increase_progress_bar()
            img_file.close()
        except OSError: # When image name is not extracted properly, we use our own image name as image[imageCounter].jpg
            img_file = open(os.path.join(dir, "image"+str(randint(1,9999))+".jpg"), "wb")
            img_file.write(img_data.content)
            print(f"Image '{img_name}' downloaded.")
            img_file.close()    
        end = time.perf_counter()
        return f"took {round(end-start, 2)} seconds"

    def display_error(self):
        if self.success_label is not None:
            self.success_label.grid_forget()
        self.error_label = Label(self.root, text=self.error_message, fg="RED")
        self.error_label.grid(row=2, column=0, columnspan= 3)

    def display_success(self):
        if self.error_label is not None:
            self.error_label.grid_forget()
        self.success_label = Label(self.root, text=self.success_message, fg="LIME")
        self.success_label.grid(row=2, column=0, columnspan=3)

    def remove_component(self, *comps:Label | Button | Entry):
        for comp in comps:
            comp.grid_forget()

    def download_button_clicked(self):
        print("Download Button Clicked")
        self.url = self.url_input.get() # Get the input from the text box
        image_urls = self.get_image_urls() # get the list of images urls from the image tags
        if image_urls is None: # if unable to get any image urls
            return
        else: # Success in getting image urls
            self.image_urls = image_urls 
            self.success_message = "Connected to URL"
            self.each_image_download_weight = (1/len(self.image_urls)*100) # How much the loading moves on each image download.
            self.display_success() # display Connected to URL in the window
            self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=100, mode="determinate")
            self.progress_bar.grid(row=3, column=0, columnspan=3, pady=10)

            self.pause_button.grid(row=5, column=0, pady=20)
            self.resume_button.grid(row=5, column=1)
            self.cancel_button.grid(row=5, column=2)

            # Starting the image download process
            image_downloading_threads = []
            for image_url in image_urls:
                image_downloading_threads.append(threading.Thread(target=self.save_image, args=[image_url]))
            
            for image_thread in image_downloading_threads:
                image_thread.start()

    def increase_progress_bar(self):
        self.progress_bar['value'] += self.each_image_download_weight

def main():
    win = Window(Tk())
    win.window()
    win.root.mainloop()


if __name__ == "__main__":
    main()