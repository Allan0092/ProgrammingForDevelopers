import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time
from random import randint
import concurrent.futures

def get_image_urls(url=""):
    html_data = requests.get(url) # sends the get request to the given url  
    print(html_data.status_code) # prints the status code
    soup = BeautifulSoup(html_data.text, 'html.parser') # Parses the html tags
    img_tags = soup.find_all("img") # finds all the img tags
    img_urls = []
    for img_tag in img_tags: # Iterate through img tags
        img_url = urljoin(url, img_tag.get("src"))
        img_urls.append(img_url)
    return img_urls

def save_images(img_urls=[], dir="Images"):
    start = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(save_image, img_urls)
    for result in results:
        print(result)

    end = time.perf_counter()
    return f"Took {round(end-start, 2)} seconds"
    
def save_image(img_url="", dir="Images"):

    start = time.perf_counter()
    os.makedirs(dir, exist_ok=True) # Create output directory if it doesn't exist
    img_name = img_url.split("/")[-1] # discards the url to get only the image name
    # Download image
    img_data = requests.get(img_url) # Request for image
    try: # when the image name can be extracted easily
        img_file = open(os.path.join(dir, img_name), "wb")
        img_file.write(img_data.content)
        print(f"Image '{img_name}' downloaded.")
        img_file.close()
    except OSError: # When image name is not extracted properly, we use our own image name as image[imageCounter].jpg
        img_file = open(os.path.join(dir, "image"+str(randint(1,9999))+".jpg"), "wb")
        img_file.write(img_data.content)
        print(f"Image '{img_name}' downloaded.")
        img_file.close()    
    end = time.perf_counter()
    return f"took {round(end-start, 2)} seconds"

def getData(url, dir="Images"):
    """get the images from the given URL

    Args:
        url (str): The url of the page
        dir (str, optional): the folder where the images will be saved. Defaults to "Images".
    """
    start = time.perf_counter()
    os.makedirs(dir, exist_ok=True) # Create output directory if it doesn't exist

    html_data = requests.get(url) # sends the get request to the given url  
    print(html_data.status_code) # prints the status code
    soup = BeautifulSoup(html_data.text, 'html.parser') # Parses the html tags
    img_tags = soup.find_all("img") # finds all the img tags
    imageCounter = 0 # for counting the number of images extracted
    for img_tag in img_tags: # Iterate through img tags
        img_url = urljoin(url, img_tag.get("src"))
        img_name = img_url.split("/")[-1] # discards the url to get only the image name
        imageCounter+=1
        # Download image
        img_data = requests.get(img_url) # Request for image
        try: # when the image name can be extracted easily
            img_file = open(os.path.join(dir, img_name), "wb")
            img_file.write(img_data.content)
            print(f"Image '{img_name}' downloaded.")
            img_file.close()
        except OSError: # When image name is not extracted properly, we use our own image name as image[imageCounter].jpg
            img_file = open(os.path.join(dir, "image"+str(imageCounter)+".jpg"), "wb")
            img_file.write(img_data.content)
            print(f"Image '{img_name}' downloaded.")
            img_file.close()

    end = time.perf_counter()
    return f"Downloaded all images at {round(end-start, 2)} seconds"