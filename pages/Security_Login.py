import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# ✅ Page config must be at the top
st.set_page_config(page_title="Security Login", layout="wide", page_icon="🛡")

st.title("Security Login")

# Input fields for login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Check login
if st.button("Login"):
    st.success(f"Logged in as {username}")
    st.session_state["security_logged_in"] = True
    st.session_state["username"] = username
    switch_page("Security_Dashboard")  # ✅ Redirects to the dashboard
