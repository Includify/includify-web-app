import streamlit as st

from routes.appointments import appointments_page
from routes.home import home_page
from routes.resources import resources_page
from routes.add_resource import add_resource_page

st.sidebar.title("Navigate to...")
page = st.sidebar.radio("Go to", ["Home", "Appointments", "Add A Resource", "Resources"], label_visibility='hidden')


if page == "Home":
    home_page()

elif page == "Appointments":
    appointments_page()

elif page == "Resources":
    resources_page()

elif page == "Add A Resource":
    add_resource_page()
