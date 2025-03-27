import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import datetime
from model import predict_class
# ✅ Page config
st.set_page_config(page_title="Report Incident", layout="wide", page_icon="📹")

st.title("Report an Incident")

# Initialize session state storage for incidents
if "incident_reports" not in st.session_state:
    st.session_state["incident_reports"] = []

# File uploader for video
uploaded_file = st.file_uploader("Upload incident clip", type=["mp4", "mov", "avi"])

# 📌 Get User Location
location = streamlit_js_eval(
    js_expressions="new Promise((resolve) => navigator.geolocation.getCurrentPosition((pos) => resolve({latitude: pos.coords.latitude, longitude: pos.coords.longitude})))", 
    want_output=True
)
latitude, longitude = None, None
if location:
    latitude = location["latitude"]
    longitude = location["longitude"]
    st.write(f"Your Location: **({latitude}, {longitude})**")

# Simulated classification (Replace with actual AI classification)
classified_class = predict_class(uploaded_file)

# ✅ Submit button
if st.button("Submit Report"):
    if uploaded_file and latitude and longitude:
        # ✅ Store report locally in session state
        report_data = {
            "username": st.session_state.get("username", "Unknown"),
            "file_name": uploaded_file.name,
            "class_name": classified_class,
            "location": {"latitude": latitude, "longitude": longitude},
            "timestamp": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        }

        st.session_state["incident_reports"].append(report_data)
        st.success("Incident reported successfully!")

    else:
        st.error("Please upload a clip and allow location access.")
