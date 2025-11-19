
# 1. **Title and Slider**:
#    ```python
#    st.markdown("# Temperature Converter")
#    temperature = st.slider("Select temperature in Celsius", -100, 100)
#    st.markdown(f"Temperature in Fahrenheit: {temperature * 9/5 + 32}")
#    ```


import streamlit as st



# temperature converter

# increase number of # in markdown thinner the content
st.markdown("# Temperature converter")


# slider 
temperature = st.slider("Select the temperature in Celsius", -100 , 100)
st.markdown(f"Temperature in Fehrenheit :{temperature *9/5 +32}")