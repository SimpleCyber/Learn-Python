import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load environment variables from .env file
load_dotenv()

# Access the CHROMEDRIVER_PATH from environment variables
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")

# Set up the Chrome service with the path to ChromeDriver
service = Service(executable_path=chromedriver_path)

# Set up options for Chrome to connect to the already open session
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Set up WebDriver to connect to the existing Chrome session
driver = webdriver.Chrome(service=service, options=chrome_options)

# Go to the Liked Videos playlist
driver.get("https://www.youtube.com/playlist?list=LL")
time.sleep(5)

# Loop through each video in the playlist and dislike them
while True:
    try:
        # Wait for video to be clickable
        video = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-playlist-video-renderer.style-scope"))
        )
        
        # Scroll to the video
        driver.execute_script("arguments[0].scrollIntoView(true);", video)

        # Use JavaScript to click the video if standard click does not work
        driver.execute_script("arguments[0].click();", video)

        # Wait for the like button to load and click to dislike
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-toggle-button-renderer.style-scope:nth-child(1)"))
        )
        
        # Scroll to the like button
        driver.execute_script("arguments[0].scrollIntoView(true);", like_button)
        
        # Use JavaScript to click the like button if standard click does not work
        driver.execute_script("arguments[0].click();", like_button)

        time.sleep(2)  # Wait a bit before moving to the next video

        # Go back to playlist
        driver.back()
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Close the browser when done
driver.quit()
