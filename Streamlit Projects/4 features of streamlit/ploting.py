# 18. **Interactive Plotting with Altair**

# :
#     ```python
#     st.markdown("## Interactive Chart")
#     data = load_chart_data()  # Load your data
#     chart = alt.Chart(data).mark_line().encode(x='x', y='y')
#     st.altair_chart(chart, use_container_width=True)
#     ```


import streamlit as st 

st.markdown("## Interactive Chart")
data = load_chart_data()  # Load your data
chart = alt.Chart(data).mark_line().encode(x='x', y='y')
st.altair_chart(chart, use_container_width=True)
#  