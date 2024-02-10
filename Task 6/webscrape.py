import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def getData(url, dir="Images"):
    # Create output directory if it doesn't exist
    os.makedirs(dir, exist_ok=True)

    html_data = requests.get(url)    
    print(html_data.status_code)
    soup = BeautifulSoup(html_data.text, 'html.parser')
    img_tags = soup.find_all("img")
    imageCounter = 0
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag.get("src"))
        img_name = img_url.split("/")[-1]
        imageCounter+=1
        # Download image
        img_data = requests.get(img_url)
        try:
            img_file = open(os.path.join(dir, img_name), "wb")
            img_file.write(img_data.content)
            print(f"Image '{img_name}' downloaded.")
            img_file.close()
        except OSError:
            img_file = open(os.path.join(dir, "image"+str(imageCounter)+".jpg"), "wb")
            img_file.write(img_data.content)
            print(f"Image '{img_name}' downloaded.")
            img_file.close()
