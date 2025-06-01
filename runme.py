#This file is critical for the app as it enables to make connection with the different files and the navigation between the different feature of the app
# Import Streamlit for creating the web app
import streamlit as st
# Import the main functions from our modules:
# club_finder: provides a the ai powered search interface for clubs
# clubs_visu: provides visualization dashboards for clubs and the list of the clubs
from OPENAIAPI import main as club_finder
from Clubsvisu import main as clubs_visu

# Configure the overall page settings before any UI elements are rendered
# page_title: displayed in the browser tab
# layout: 'wide' allows using the full width of the page
st.set_page_config(
    page_title="Student Clubs App",  # Title shown in the browser window
    layout="wide"                  # Use the entire width for content
)

# Sidebar for the navigation between the two different pages 
# Display a sidebar title to group navigation controls
st.sidebar.title("Navigate")
# Create a selector in the sidebar for switching between pages
page = st.sidebar.radio(
    "Go to",                      
    ["Club Finder", "Clubs Visualization and List"]  # options for navigation according to the two different pages
)

# fonction that manage what to present according to the user choice
if page == "Club Finder":
    # If 'Club Finder' is selected, call the club_finder() function
    club_finder()
else:
    # Otherwise, run the clubs_visu() function for visualizations
    clubs_visu()

