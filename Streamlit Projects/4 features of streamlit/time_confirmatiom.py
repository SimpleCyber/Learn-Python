# 14. **Time Input and Confirmation**:
#     ```python
#     st.markdown("## Appointment Scheduler")
#     time = st.time_input("Select a time for your appointment")
#     st.markdown(f"Appointment Time: `{time}`")
#     ```


import streamlit as  st

st.markdown("## Appointment Scheduler")
time = st.time_input("Select a time for your appointment")
st.markdown(f"Appointment Time: `{time}`")
if time  :
    st.write("hello moto")