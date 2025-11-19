from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.service import Service


# Access credentials from environment variables
username = os.getenv("YOUTUBE_EMAIL")
password = os.getenv("YOUTUBE_PASSWORD")
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")



service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Assuming driver is already set up
driver.get("https://www.youtube.com")

# Wait for the "Sign in" button and click it
try:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign in')]"))
    )
    sign_in_button.click()
except Exception as e:
    print(f"Error finding the Sign in button: {e}")
