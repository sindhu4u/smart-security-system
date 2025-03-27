import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Set up Streamlit page configuration
st.set_page_config(page_title="Home - Security Alert System",layout="wide", page_icon="🏠")

# Sidebar with logo and project description
st.sidebar.image("logo.jpg", use_container_width=True)
st.sidebar.title("Security Alert System")
st.sidebar.write(
    "Our AI-driven campus security system provides real-time threat detection and rapid emergency response. "
    "With real-time monitoring, our app allows students to send instant SOS alerts with location data and "
    "allows security personnel to view alert locations and video clips. By automating alerts and providing "
    "immediate access to critical information, we aim to significantly enhance campus safety by facilitating "
    "faster response times and improved situational awareness."
)

# Home Page Content
st.title("Welcome to our Security Alert System!")
st.write(
    "For students, you can simply log in and in an emergency, tap the SOS button to instantly send your location to security. "
    "Security personnel can log in to view a map of active SOS alerts and access relevant video clips. "
    "Your communication and response during campus emergencies will help in keeping our community safe!"
)

# Centering the button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Proceed to Login"):
        st.switch_page("pages/Login_Selection.py")


hide_sidebar_style = """
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)