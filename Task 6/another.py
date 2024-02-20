import asyncio
import aiohttp
import tkinter as tk
from tkinter import ttk
from concurrent.futures import ThreadPoolExecutor

from webscrape import get_image_urls, save_image

class ImageDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Async Image Downloader")

        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        self.download_button = ttk.Button(root, text="Download Images", command=self.download_images)
        self.download_button.pack()

        self.progress_label = ttk.Label(root, text="")
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack()

        self.executor = ThreadPoolExecutor(max_workers=5)

    def download_images(self):
        url = self.url_entry.get()
        asyncio.run(self.download_images_async(url))

    async def download_images_async(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                response = await session.get(url)
                if response.status == 200:
                    html = await response.text()
                    # Extract image URLs from HTML (you can use BeautifulSoup or other libraries)
                    image_urls = get_image_urls(url)
                    # image_urls = ["url1", "url2", "url3"]  # Placeholder for image URLs
                    total_images = len(image_urls)
                    downloaded_images = 0
                    self.progress_label.config(text="Downloading...")
                    for image_url in image_urls:
                        await self.download_image(session, image_url)
                        downloaded_images += 1
                        self.progress_label.config(text=f"Downloaded {downloaded_images}/{total_images} images")
                        self.progress_bar['value'] = (downloaded_images / total_images) * 100
                    self.progress_label.config(text="Download complete")
                else:
                    self.progress_label.config(text=f"Failed to fetch URL: {url}")
            except Exception as e:
                self.progress_label.config(text=f"Error: {e}")

    async def download_image(self, session, image_url):
        async with session.get(image_url) as response:
            if response.status == 200:
                # Save the image to disk or do any other processing
                save_image(image_url)
            else:
                raise Exception(f"Failed to download image: {image_url}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDownloader(root)
    root.mainloop()
