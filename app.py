import streamlit as st
st.title("AI enabled web application")
st.write("This is a simple web application built using Streamlit and powered by AI.")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}! Welcome to the AI enabled web application.")