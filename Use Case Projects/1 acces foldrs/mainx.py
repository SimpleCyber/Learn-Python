import random
import webbrowser
from time import sleep

# List of search terms
search_terms = [
    "python programming",
    "latest tech news",
    "how to bake a cake",
    "best travel destinations",
    "machine learning tutorials",
    "top movies of 2023",
    "weather today",
    "learn data science",
    "healthy recipes",
    "sports news"
]

# Function to perform a search
def perform_search(query):
    url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
    webbrowser.get(using='microsoft-edge').open_new_tab(url)

# Perform 1 random search every hour for 24 hours
for _ in range(24):
    search_query = random.choice(search_terms)
    perform_search(search_query)
    sleep(3600)  # Wait for 1 hour before the next search
