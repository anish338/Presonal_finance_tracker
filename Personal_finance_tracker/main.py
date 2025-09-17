import streamlit as st
from app import Finance_Tracker

st.title("WELCOME TO YOUR PERSONAL FINANCE TRACKER")


if "FT" not in st.session_state:
    st.session_state.FT = Finance_Tracker()

FT = st.session_state.FT