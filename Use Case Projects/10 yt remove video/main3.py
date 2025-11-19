import pyautogui
import time

# Click positions recorded
click_positions = [(1844, 574), (1713, 877) , (1844, 574), (1713, 835)]

# Number of times to repeat the clicks
repeat_count = 40

# Delay between clicks (in seconds)
delay = 1

# Function to perform clicks at recorded positions
def perform_clicks():
    for i in range(repeat_count):
        for position in click_positions:
            pyautogui.click(position)
            time.sleep(delay)  # Optional delay between clicks

# Give yourself time to switch to the right window
print("You have 10 seconds to switch to the target window.")
time.sleep(10)

# Perform the clicks
perform_clicks()

print("Finished clicking.")
