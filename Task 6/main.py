import asyncio
import tkinter as tk
import webscrape as WS
import time
import concurrent.futures



def main_window():
    global root
    root = tk.Tk()
    root.title("Download Image")

    title_label = tk.Label(root, text="Download All Images")
    title_label.grid(row=0, column=0, columnspan=3)

    input_label = tk.Label(root, text="URL 1:")
    input_label.grid(row=2, column=0, pady=10)
    input_entry = tk.Entry(root)
    input_entry.grid(row=2, column=1, padx=20, pady=10, ipadx=30)


    def retrieve_input():
        input1 = input_entry.get()
        download_button_clicked(input1)

    
    button = tk.Button(root, text="Download", command=retrieve_input)
    button.grid(row=20, columnspan=2, pady=(0,20))

    root.mainloop()

def show_progress(message=""):
    global progress_label 
    progress_label = tk.Label(root, text=message)
    progress_label.grid(row = 21, column= 0, pady=5,columnspan=4)


def remove_Label(label=tk.Label):
    label.grid_forget()


def download_button_clicked(url):
    image_urls = WS.get_image_urls(url)
    total_imgs = len(image_urls)
    show_progress(f"downloading 0 of {total_imgs} images.")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start = time.perf_counter
        results = [executor.submit(WS.save_image, image_url) for image_url in image_urls]
        for result in concurrent.futures.as_completed(results):
            print(result.result())
    end=time.perf_counter
    show_progress(f"Finished in {round(end-start, 2)} second(s)")
    # remove_Label(progress_label)

def testing():
    start = time.perf_counter()
    urls = ["https://www.yetitrailadventure.com/", "https://www.anepaltrek.com/activities-category/annapurna-trekking/", "https://www.lonelyplanet.com/nepal"]
    # WS.getData(urls[2])
    image_urls = []
    # for url in urls:
    #     image_urls.extend(WS.get_image_urls(url))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = (list(executor.map(WS.get_image_urls, urls)))
        for result in results:
            image_urls.extend(result)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(WS.save_image, image_urls)

    for result in results:
        print(result)
    end = time.perf_counter()
    print(f"Finished at {round(end-start,2)} seconds")

def getFolderName(url):
    return url.split(".")[1]


def main():
    main_window()


if __name__ == "__main__":
    main()