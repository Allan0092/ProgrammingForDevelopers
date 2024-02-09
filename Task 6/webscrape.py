import requests
from bs4 import BeautifulSoup


def getData(url):
    html_data = requests.get(url)    
    print(html_data.status_code)
    soup = BeautifulSoup(html_data.text, 'html.parser')
    img_tags = soup.find_all("img")
    # print(img_tags)

    for image in img_tags:
        print(image)
