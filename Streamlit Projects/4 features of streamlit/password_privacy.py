# 15. **Password Input and Privacy Note**:
#     ```python
#     password = st.text_input("Enter your password:", type="password")
#     st.markdown("Your password is kept confidential.")
#     ```

import streamlit as st

password = st.text_input("Enter your password:", type="password")
st.markdown("Your password is kept confidential.")
   