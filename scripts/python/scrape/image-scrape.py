import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the URL to scrape
url = "https://example.com"  # Replace with the target website

# Send a GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Create a directory for images
os.makedirs("images", exist_ok=True)

# Find and download images
for img_tag in soup.find_all("img"):
    img_url = img_tag.get("src")
    if not img_url:
        continue

    # Convert relative URLs to absolute
    img_url = urljoin(url, img_url)

    # Get the image content
    img_data = requests.get(img_url).content
    img_name = os.path.join("images", os.path.basename(img_url))

    # Save the image
    with open(img_name, "wb") as img_file:
        img_file.write(img_data)

    print(f"Downloaded: {img_name}")
