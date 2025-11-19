# 10. **Radio Buttons for Navigation**:
#     ```python
#     st.markdown("# Dashboard")
#     page = st.radio("Select a page:", ["Home", "About", "Contact"])
#     if page == "Home":
#         st.markdown("Welcome to the Home Page!")
#     elif page == "About":
#         st.markdown("Learn more about us.")
#     ```



import streamlit as st 

st.markdown("# Dashboard")
page = st.radio("Select a page:", ["Home", "About", "Contact"])
if page == "Home":
    st.markdown("Welcome to the Home Page!")
elif page == "About":
    st.markdown("Learn more about us.")
else:
    st.markdown("satyam contact me +91 7840935392")
    