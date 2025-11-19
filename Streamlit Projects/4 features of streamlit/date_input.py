# 5. **Date Picker and Display**:
#    ```python
#    st.markdown("## Event Planner")
#    date = st.date_input("Select a date for the event")
#    st.markdown(f"Event Date: {date.strftime('%A, %B %d, %Y')}")
#    ```

import streamlit as st  

st.markdown("## Event Planner")

date = st.date_input("Select a date for the event")

st.markdown(f"Event Date :{date.strftime('%A , %B %d, %Y')}")