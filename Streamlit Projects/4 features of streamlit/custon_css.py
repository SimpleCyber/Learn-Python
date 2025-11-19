# 20. **Custom CSS Styling with Markdown**:
#     ```python
#     st.markdown("""
#         <style>
#         .big-font {
#             font-size:50px !important;
#         }
#         </style>
#         """, unsafe_allow_html=True)
#     st.markdown('<p class="big-font">Big Text</p>', unsafe_allow_html=True)
#     ```



import streamlit as st
if True :

    st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
            margin :100px;
            
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Big Text</p>', unsafe_allow_html=True)
