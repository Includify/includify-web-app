import datetime
import os

import streamlit as st
import service
from dotenv import load_dotenv


def format_days_binary(selected_days):
    days_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return ''.join(['1' if day in selected_days else '0' for day in days_order])

def time_to_millis(time_obj):
    return (time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second) * 1000

def add_resource_page():
    st.markdown("""
        <style>
        /* Form Container */
        .form-container {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: auto;
        }

        /* Input Styling */
        .stTextInput, .stTextArea, .stMultiSelect {
            font-size: 1rem !important;
        }

        /* Button Styling */
        .stButton button {
            background: #3498db;
            color: white;
            font-size: 1rem;
            padding: 0.7rem 1.5rem;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: #2980b9;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #2c3e50;'>Add A New Resource</h2>", unsafe_allow_html=True)

    categories = [
        "Visually Challenged", "Speech Impaired", "Hearing Impaired",
        "Upper Limb Impaired", "Lower Limb Impaired", "Senior Citizens"
    ]

    with st.form("add_resource_form"):
        st.markdown("**Enter Details**")

        title = st.text_input("Resource Title")
        description = st.text_area("Description", height=150)
        usage_instructions = st.text_area("Usage Instructions", height=150)
        target_users = st.multiselect("Target User Categories", categories)

        st.write("")
        st.markdown("**Availability (Specific Date OR Weekly days)**")
        date = st.date_input("Select Date", min_value="today")

        st.markdown("-OR-")
        days_of_week = st.multiselect("Select Days of the Week",
                                      ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

        now = datetime.datetime.now()
        default_end_time = (now + datetime.timedelta(hours=1)).time()
        start_time = st.time_input("Start Time", now.time())
        end_time = st.time_input("End Time", default_end_time)

        st.write("")
        st.write("")
        submitted = st.form_submit_button("Add Resource")

        if submitted:
            if not title or not description or not usage_instructions or not target_users or (not days_of_week and not date):
                st.error("Please fill in all fields before submitting.")

            else:
                formatted_date = date.strftime("%m%d%Y") if date else "N/A"

                binary_days = format_days_binary(days_of_week)
                start_time_millis = time_to_millis(start_time)
                end_time_millis = time_to_millis(end_time)
                selected_indices = [str(categories.index(category) + 1) for category in target_users]

                request_body = {
                    "organisationId": "fe844beb-13d9-473c-89c6-31dc452086fd",
                    "resourceTypeIds": [
                        "3"
                    ],
                    "targetUserCategoryIds": selected_indices,
                    "title": title,
                    "description": description,
                    "usageInstructions": usage_instructions,
                    "resourceService": {
                        "timeStart": start_time_millis,
                        "timeEnd": end_time_millis,
                        "date": formatted_date,
                        "days": binary_days
                    }
                }

                load_dotenv()
                resp = service.add_resource(request_body, os.getenv('jwt_token'))

                if resp:
                    st.success(f"✅ Resource '{title}' added successfully!")
                else:
                    st.error("Something went wrong.")






