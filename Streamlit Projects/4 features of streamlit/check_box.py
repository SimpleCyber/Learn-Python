
# 4. **Using Checkboxes to Reveal More Info**:
#    ```python
#    if st.checkbox("Show more information"):
#        st.markdown("Here is some more information about this topic.")
#    ```


import streamlit as st 

if st.checkbox("Show more information"):
    st.markdown("Here is some more information about this topic.")  

