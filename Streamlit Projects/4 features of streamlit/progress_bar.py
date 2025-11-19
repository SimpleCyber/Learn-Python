# 16. **Progress Bar and Process Explanation**:
#     ```python
#     import time
#     st.markdown("## Processing Data")
#     progress_bar = st.progress(0)
#     for i in range(100):
#         time.sleep(0.1)
#         progress_bar.progress(i + 1)
#     st.markdown("Data processing complete!")
#     ```



import time
import streamlit as st
if True:
    st.markdown("## Processing Data")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress_bar.progress(i + 1)
    st.markdown("Data processing complete!")
