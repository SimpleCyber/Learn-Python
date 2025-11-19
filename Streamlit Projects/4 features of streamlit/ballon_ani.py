# 24. **Balloon Animation on Event**:
#     ```python
#     if st.button("Celebrate!"):
#         st.balloons()
#         st.markdown("🎉 Celebration Time!")
#     ```


import streamlit as st
if True:

    if st.button("Celebrate!"):
        st.balloons()
        st.divider()
        x= "hello moto"
        st.chat_message( x )
        st.chat_message( x )
        st.snow()
        
        st.markdown("🎉 Celebration Time!")



        
def model(x):
    return x
if True:
    st.markdown("## Make a Prediction")
    input_data = st.text_input("Enter input data for prediction:")
    if st.button("Predict"):
        prediction = model.predict(input_data)  # Assume a prediction model
        st.markdown(f"Prediction: {prediction}")