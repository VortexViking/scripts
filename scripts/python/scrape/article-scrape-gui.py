import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup

# Function to scrape the website and display the result
def scrape_website():
    url = entry.get()
    
    # Send a GET request to fetch the webpage
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract text content from the page
            text = soup.get_text(separator="\n", strip=True)
            
            # Display the extracted text in the text box
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, text)
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Failed to retrieve the webpage: {response.status_code}")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("VortexViking Web Scraper")
root.geometry("600x500")
root.configure(bg="#222222")

# Style elements for VortexViking theme
font = ("Arial", 12)
button_bg = "#ff4c4c"  # Red color for buttons
entry_bg = "#333333"  # Dark background for input fields
text_bg = "#1f1f1f"   # Dark background for text area
text_fg = "#ffffff"   # White text

# Title Label
title_label = tk.Label(root, text="VortexViking Web Scraper", font=("Arial", 20, "bold"), fg="#ff4c4c", bg="#222222")
title_label.pack(pady=20)

# URL input field
entry_label = tk.Label(root, text="Enter URL to scrape:", font=font, fg="#ffffff", bg="#222222")
entry_label.pack(pady=5)
entry = tk.Entry(root, font=font, width=50, bg=entry_bg, fg="#ffffff")
entry.pack(pady=5)

# Scrape Button
scrape_button = tk.Button(root, text="Scrape", font=font, bg=button_bg, fg="#ffffff", command=scrape_website)
scrape_button.pack(pady=15)

# Scrolled Text Box to display result
result_text = scrolledtext.ScrolledText(root, font=font, width=70, height=15, bg=text_bg, fg=text_fg)
result_text.pack(pady=10)

# Run the GUI
root.mainloop()
