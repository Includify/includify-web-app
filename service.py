import requests
import streamlit as st


def get_company_data():
    try:
        response = requests.get("http://localhost:8080/organisation/fe844beb-13d9-473c-89c6-31dc452086fd")
        data = response.json()
        return data
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None


def get_resource_details(id):
    try:
        response = requests.get(f"http://localhost:8080/resource/{id}")
        data = response.json()
        return data
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

def get_appointments(token):
    url = "http://localhost:8080/appointment/organisation?organisation=fe844beb-13d9-473c-89c6-31dc452086fd"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None


def add_resource(resource_data, token):
    url = "http://localhost:8080/resource/add"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=resource_data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding resource: {str(e)}")
        return None