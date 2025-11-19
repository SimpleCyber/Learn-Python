# 17. **Interactive Image Display**:
#     ```python
#     st.markdown("### Select an Image")
#     image_option = st.selectbox("Choose an image:", ["Nature", "City", "Space"])
#     image = load_image(image_option)  # Assuming a function to load images
#     st.image(image, caption=image_option)
#     ```


import streamlit as st

def load_image(x):
    if x == "Nature":
        return 'IMG_20230924_092620.jpg'


if True:
    st.markdown("### Select an Image")
    image_option = st.selectbox("Choose an image:", ["Nature", "City", "Space"])
    image = load_image(image_option)  # Assuming a function to load images
    st.image(image, caption=image_option)
