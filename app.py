# app.py
import streamlit as st
from Full import main as club_finder
from Clubsvisu import main as clubs_visu

st.set_page_config(page_title="Student Clubs App", layout="wide")
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Club Finder", "Clubs Visualization"])

if page == "Club Finder":
    club_finder()
else:
    clubs_visu()



