# PYTHON WEB SCRAPER
# By VortexViking
# February 6th, 2025
# 5:39 PM
# EXAMPLE USING HACKER NEWS URL

# Imports
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    url = "https://news.ycombinator.com/item?id=29782099"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind")  # Fixed class selection
    comments = [e.find_next(class_="comment") for e in elements]
    
    keywords = {
        "python": 0,
        "javascript": 0,
        "typescript": 0,
        "ruby": 0,
        "java": 0,
        "rust": 0,
        "c#": 0,
    }
    
    print(f"Scraping {url}")
    
    for comment in comments:
        if comment:  # Ensuring the comment exists before processing
            comment_text = comment.get_text(strip=True).lower()  # Removing HTML tags and extra spaces
            words = comment_text.split(" ")  # Splitting comment text into words
            words = {w.strip(",./@#!$%^&*|") for w in words}  # Cleaning punctuation from words
            print(words)

            for k in keywords:
                if k in words:
                    keywords[k] += 1  # Fixing increment operator
    
    print(keywords)
    
    # Plotting the results
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Programming Language")
    plt.ylabel("Number of Mentions")
    plt.title("Programming Language Mentions in Hacker News Comments")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()
