import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# ✅ Page config
st.set_page_config(page_title="Student Login", layout="wide", page_icon="🧑‍🎓")

st.title("Student Login")

# Input fields for login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Check login
if st.button("Login"):
    st.success(f"Logged in as {username}")
    st.session_state["student_logged_in"] = True
    st.session_state["username"] = username
    switch_page("Student_Dashboard")  # ✅ Redirects to the Student Dashboard
