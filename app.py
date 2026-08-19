import streamlit as st

st.set_page_config(
    page_title="Football Management System",
    page_icon="⚽"
)

st.title("⚽ Football Management System")

st.subheader("Player and Team Management Portal")

st.write("Welcome to the Football Management System.")
st.write("Please login to continue managing your football team.")

st.header("Manager Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful!")
        st.write("Welcome to the Football Management Dashboard.")
    else:
        st.error("Invalid username or password.")