import random
from nudenet import NudeDetector
import streamlit as st
from PIL import Image
import os

# Get a random image file name
a = random.sample(range(1, 11), 1)
x = str(a[0])
string = x + ".jpg"

# Initialize NudeDetector
detector = NudeDetector()
data = detector.detect(string)
# Function to check if the image file exists and is readable
def check_image_exists(file_name):
    return os.path.isfile(file_name)

# if check_image_exists(string):
#     # Detect nudity in the image
#     # data = detector.detect(string)
# else:
#     data = None

# Streamlit app setup
st.markdown("# NSFW Detector")
st.write(f"File: {string}")

# Display detection data if available
if data:
    st.write(data)
else:
    st.write("Image file not found or unreadable.")

def load_image(file_name):
    # Function to load an image file
    return Image.open(file_name)

# Button to trigger image display
if st.button('Try Out'):
    if check_image_exists(string):
        image = load_image(string)
        st.image(image, caption="Your Choice")
        st.write(detector.detect(string))
    else:
        st.write("Image file not found or unreadable.")
