# 22. **Select Slider for Options**:
#     ```python
#     st.markdown("### Choose a Level")
#     level = st.select_slider("Level", options=['Easy', 'Medium', 'Hard'])
#     st.markdown(f"You selected: {level}")
#     ```



import streamlit as st 

if True :

    st.markdown("### Choose a Level")
    level = st.select_slider("Level", options=['Easy', 'Medium', 'Hard'])
    st.markdown(f"You selected: {level}")
