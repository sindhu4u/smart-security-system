import streamlit as st
import folium
from streamlit_folium import folium_static
from streamlit_extras.switch_page_button import switch_page

# ✅ Page config must be at the top
st.set_page_config(page_title="Security Dashboard", layout="wide", page_icon="🛡")

# Ensure the user is logged in
if not st.session_state.get("security_logged_in"):
    st.warning("Please log in first!")
    switch_page("Security_Login")

st.title(f"Welcome, {st.session_state['username']}!")
st.subheader("Security Dashboard")

# Example SOS alerts
sos_alerts = [
    {"user": "Student1", "latitude": 12.9716, "longitude": 77.5946, "timestamp": "2025-03-26 12:00"},
    {"user": "Student2", "latitude": 13.0827, "longitude": 80.2707, "timestamp": "2025-03-26 12:30"},
    {"user": "Student3", "latitude": 19.0760, "longitude": 72.8777, "timestamp": "2025-03-26 13:00"},
]

video_clips = ["test1.mp4", "test2.mp4", "test3.mp4", "test4.mp4"]

# SOS Alerts Map
st.subheader("🗺 SOS Alerts Map")
map_center = [sos_alerts[0]["latitude"], sos_alerts[0]["longitude"]]
alert_map = folium.Map(location=map_center, zoom_start=5)

for alert in sos_alerts:
    folium.Marker(
        [alert["latitude"], alert["longitude"]],
        popup=f"{alert['user']} - {alert['timestamp']}",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(alert_map)

folium_static(alert_map)

# View Video Clips
st.subheader("🎥 Incident Video Clips")
for video in video_clips:
    st.video(video)

# Sign Out Button
if st.button("🔙 Sign Out"):
    st.session_state["security_logged_in"] = False
    switch_page("Home")
