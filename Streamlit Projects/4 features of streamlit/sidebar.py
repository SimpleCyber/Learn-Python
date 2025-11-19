
# 11. **Sidebar with Markdown Introduction**:
#     ```python
#     st.sidebar.markdown("## Navigation Panel")
#     page = st.sidebar.selectbox("Choose a page:", ["Home", "Profile", "Settings"])
#     ```


import streamlit as st 

st.sidebar.markdown("## Navigation Panel")
page = st.sidebar.selectbox("Choose a page:", ["Home", "Profile", "Settings"])