import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_js_eval import streamlit_js_eval  

# ✅ Page config
st.set_page_config(page_title="Student Dashboard", layout="wide", page_icon="🎓")

# Ensure the user is logged in
if not st.session_state.get("student_logged_in"):
    st.warning("Please log in first!")
    switch_page("Student_Login")

st.title(f"Welcome, {st.session_state['username']}!")
st.subheader("Student Dashboard")

# 📌 Capture Location (Better method)
location = streamlit_js_eval(
    js_expressions="new Promise((resolve) => navigator.geolocation.getCurrentPosition((pos) => resolve({latitude: pos.coords.latitude, longitude: pos.coords.longitude})))", 
    want_output=True
)

# ✅ Send SOS Alert Button
if st.button("🚨 Send SOS Alert"):
    if location:
        st.success(f"SOS Alert sent! 📍 Location: {location['latitude']}, {location['longitude']}")
    else:
        st.error("Failed to get location. Please enable GPS and try again.")

# ✅ Report Incident Button (Navigates to the "Report Incident" page)
if st.button("📹 Report Incident"):
    switch_page("Report_Incident")

# 🔙 Sign Out Button
if st.button("🔙 Sign Out"):
    st.session_state["student_logged_in"] = False
    switch_page("Home")
