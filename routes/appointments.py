import os

import streamlit as st
from datetime import datetime

from dotenv import load_dotenv

import service


def format_time(ms):
    if ms is None:
        return "N/A"
    return datetime.utcfromtimestamp(ms / 1000).strftime("%I:%M %p")

def format_days(date):
    if date:
        return datetime.strptime(date, '%m%d%Y').strftime('%B %d, %Y')
    return "N/A"

def appointments_page():
    st.markdown("""
        <style>
        .appointment-card {
            background-color: #f8f9fa;
            border-left: 5px solid #ff2b2b;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .appointment-title {
            font-size: 22px;
            font-weight: bold;
            color: #333;
        }
        .appointment-details {
            font-size: 16px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Upcoming Appointments")
    load_dotenv()
    appointments = service.get_appointments(os.getenv("jwt_token"))

    if len(appointments) == 0:
        st.markdown("_No appointments scheduled yet._")

    for appointment in appointments:
        titles = ", ".join(obj["title"] for obj in appointment['user']["categories"])
        resources = ", ".join(obj["title"] for obj in appointment['resources'])

        st.markdown(
            f"""
            <div class="appointment-card">
                <div class="appointment-title">{format_days(appointment['date'])}</div>
                <p class="appointment-details"><strong>START TIME<br></strong> <span class="highlight">{format_time(appointment['timeStart'])}</span></p>
                <p class="appointment-details"><strong>END TIME<br></strong> <span class="highlight">{format_time(appointment['timeEnd'])}</span></p>
                <p class="appointment-details"><strong>CLIENT NAME<br></strong> {appointment['user']['name']}</p>
                <p class="appointment-details"><strong>AGE<br></strong> {appointment['user']['age']}</p>
                <p class="appointment-details"><strong>EMAIL<br></strong> {appointment['user']['email']}</p>
                <p class="appointment-details"><strong>USER CATEGORY(S)<br></strong> {titles}</p>
                <p class="appointment-details"><strong>RESOURCE(S) BOOKED<br></strong> {resources}</p>
                <p class="appointment-details"><strong>VOLUNTEER DETAILS<br></strong>
                    {appointment['volunteer']['name']} <br>
                    {appointment['volunteer']['email']} <br>
                    {appointment['volunteer']['age']} years <br>
                    {appointment['volunteer']['address']} <br>
                    {appointment['volunteer']['phone']} <br>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )