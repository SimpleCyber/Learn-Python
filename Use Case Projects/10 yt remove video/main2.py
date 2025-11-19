import pyautogui
import time

# Click positions recorded
click_positions = [(1847, 657), (1754, 953)]

# Number of times to repeat the clicks
repeat_count = 400

# Delay between clicks (in seconds)
delay = 1

# Function to perform clicks at recorded positions and print the count
def perform_clicks():
    click_number = 1
    for _ in range(repeat_count):
        for position in click_positions:
            pyautogui.click(position)
            print(f"Click number: {click_number}")
            click_number += 1
            time.sleep(delay)  # Optional delay between clicks

# Give yourself time to switch to the right window
print("You have 10 seconds to switch to the target window.")
time.sleep(10)

# Perform the clicks
perform_clicks()

print("Finished clicking.")
