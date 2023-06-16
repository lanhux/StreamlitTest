import streamlit as st
import time


st.title("Streamlit on Lanhux's blog")

st.write("This is a sample app to show how to use Streamlit on Lanhux's repository")

st.write("if you want to use Streamlit on your bowser, you can use the following command")

st.code("pip install streamlit")

st.write("if you want to run your app, you can use the following command")

st.code("streamlit run yourapp.py")

st.write("now let's study together!")

if st.button("Next"):
    st.write("Let's go!")
    time.sleep(1)
    st.stop()


