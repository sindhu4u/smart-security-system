import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Security Alert System", layout="wide")

# Sidebar with logo and project description
st.sidebar.image("logo.jpg", use_container_width=True)
st.sidebar.title("Security Alert System")
st.sidebar.write("Our AI-driven campus security system provides real-time threat detection and rapid emergency response. With real-time monitoring, our app allows students to send instant SOS alerts with location data and allows security personnel to view alert locations and video clips. By automating alerts and providing immediate access to critical information, we aim to significantly enhance campus safety by facilitating faster response times and improved situational awareness.")

# Home Page Content
st.title("Welcome to our Security Alert System!")
st.write("Students can simply log in and in an emergency, tap the SOS button to instantly send your location to security. Security personnel can log in to view a map of active SOS alerts and access relevant video clips. Your communication and response during campus emergencies will help in keeping our community safe!")

# Navigation to Login Page
if st.button("Proceed to Login"):
    st.session_state.page = "login_selection"

# Role Selection Page
if "page" in st.session_state and st.session_state.page == "login_selection":
    st.subheader("Select Your Role")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Student Login"):
            st.session_state.page = "student_login"
    with col2:
        if st.button("Security Login"):
            st.session_state.page = "security_login"

# Student Login Page
if "page" in st.session_state and st.session_state.page == "student_login":
    st.subheader("Student Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("Logged in as Student")
        # Proceed with authentication logic

# Security Login Page
if "page" in st.session_state and st.session_state.page == "security_login":
    st.subheader("Security Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("Logged in as Security")
        # Proceed with authentication logic
