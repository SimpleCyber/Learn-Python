import random
import streamlit as st
import time



if st.button('Try Out'):
    x = int(input("Enter the number of loops :"))
    st.snow()
    
    while x>0:
        a = random.sample(range(1,11),1)
        ans = str(a)
        st.write(x, ".",end= " ")

        st.chat_message(ans[1])
        time.sleep(3)

        x -= 1

    st.balloons()
