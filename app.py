import streamlit as st
st.title("AI powered Streamlit application")
st.write("This is a web application which is AI-powered and deployed with Streamlit")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}! Welcome to the AI-powered web application.")