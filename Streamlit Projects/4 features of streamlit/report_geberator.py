# 9. **Interactive Markdown Report Generator**:
#    ```python
#    report_text = st.text_area("Write your report:")
#    if st.button("Generate Report"):
#        st.markdown(report_text)
#    ```



import streamlit as st 

report_text = st.text_area("Write your report:")
if st.button("Generate Report"):
    st.markdown(report_text)