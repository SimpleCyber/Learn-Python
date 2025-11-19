# 13. **Multi-Page Layout with Markdown**:
#     ```python
#     page = st.sidebar.radio("Select a Page:", ["Home", "Analysis", "Contact"])
#     if page == "Home":
#         st.markdown("# Welcome to the Home Page")
#     ```



import streamlit as st 


page = st.sidebar.selectbox("Select a Page:", ["Home", "Analysis", "Contact"])
if page == "Home":
    st.markdown("# Welcome to the Home Page")
if page == "Analysis":
    st.markdown("# Welcome to the Analysis Page")