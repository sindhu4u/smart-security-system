import streamlit as st

st.set_page_config(page_title="Login Selection", page_icon="🔑",layout="wide")

st.title("Select Your Role")

col1, col2 = st.columns(2)
with col1:
    if st.button("Student Login"):
        st.switch_page("pages/Student_Login.py")
with col2:
    if st.button("Security Login"):
        st.switch_page("pages/Security_Login.py")



hide_sidebar_style = """
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)