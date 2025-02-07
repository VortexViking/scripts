import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = input("What url do you want to scrape?").lower()

# Send a GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract text content from the page
    text = soup.get_text(separator="\n", strip=True)
    
    print(text)  # Display the extracted text
else:
    print("Failed to retrieve the webpage:", response.status_code)
