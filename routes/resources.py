import streamlit as st
from datetime import datetime

import service


def format_time(ms):
    if ms is None:
        return "N/A"
    return datetime.utcfromtimestamp(ms / 1000).strftime("%I:%M %p")

def format_days(days, date):
    if date:
        return f"<p class='resource-details'><strong>DATE</strong><br>{datetime.strptime(date, '%m%d%Y').strftime('%B %d, %Y')}</p>"
    elif days:
        week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        active_days = [week_days[i] for i, v in enumerate(days) if v == "1"]
        return f"<p class='resource-details'>DATE<br>{', '.join(active_days)}</p>"
    return "N/A"

def resources_page():
    st.markdown("""
        <style>
        .resource-card {
            background-color: #f8f9fa;
            border-left: 5px solid #ff2b2b;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .resource-title {
            font-size: 22px;
            font-weight: bold;
            color: #333;
        }
        .resource-details {
            font-size: 16px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Available Resources")
    resources = service.get_company_data()['resources']
    detailed_resources = []

    if len(resources) == 0:
        st.markdown("_No resources added. Add a new resource to give your viewers a more inclusive cinematic experience._")

    for resource in resources:
        detailed_resources.append(service.get_resource_details(resource['id']))

    for resource in detailed_resources:
        titles = ", ".join(obj["title"] for obj in resource['targetUserCategory'])
        types = ", ".join(obj["title"] for obj in resource['resourceType'])

        st.markdown(
            f"""
            <div class="resource-card">
                <div class="resource-title">{resource['title']}</div>
                <p class="resource-details">{resource['description']}</p>
                <p class="resource-details"><strong>USAGE INSTRUCTIONS<br></strong> {resource['usageInstructions']}</p>
                <p class="resource-details"><strong>RESOURCE TYPES<br></strong> {types}</p>
                <p class="resource-details"><strong>TARGET USER CATEGORIES<br></strong> {titles}</p>
                <p class="resource-details"><strong>START TIME<br></strong> <span class="highlight">{format_time(resource['resourceService']['timeStart'])}</span></p>
                <p class="resource-details"><strong>END TIME<br></strong> <span class="highlight">{format_time(resource['resourceService']['timeEnd'])}</span></p>
                <p class="resource-details">{format_days(resource['resourceService']['days'], resource['resourceService']['date'])}</p>
            </div>
            """,
            unsafe_allow_html=True
        )