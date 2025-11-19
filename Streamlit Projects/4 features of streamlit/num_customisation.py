# 19. **Number Input for Customization**:
#     ```python
#     st.markdown("### Customize Your Pizza")
#     slices = st.number_input("How many slices?", min_value=1, max_value=8)
#     st.markdown(f"Your pizza will have {slices} slices.")
#     ```

import streamlit as st  

st.markdown("### Customize Your Pizza")
slices = st.number_input("How many slices?", min_value=1, max_value=8)
st.markdown(f"Your pizza will have {slices} slices.")
