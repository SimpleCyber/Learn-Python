# 12. **Color Picker and Display**:
#     ```python
#     st.markdown("### Choose a Color")
#     color = st.color_picker("Pick a color")
#     st.markdown(f"Your selected color: `{color}`")
#     ```


import streamlit as st


st.markdown("### Choose a Color")
color = st.color_picker("Pick a color")
st.markdown(f"Your selected color: `{color}`")
