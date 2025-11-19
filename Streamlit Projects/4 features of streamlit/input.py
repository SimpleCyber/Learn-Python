# 6. **Text Input and Echo**:
#    ```python
#    name = st.text_input("Enter your name:")
#    if name:
#        st.markdown(f"Hello, **{name}**!")
#    ```

import streamlit as st 
name = st.text_input("Enter your name :")

if name:
    st.markdown(f"Hello ,**{name}** ! ")