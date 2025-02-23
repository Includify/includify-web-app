import datetime
import time
import streamlit as st

from streamlit_lottie import st_lottie
from lottie import load_lottie_file
from service import get_company_data

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 6 < current_hour < 12:
        return "Good Morning !!"
    elif 12 <= current_hour < 18:
        return "Good Afternoon️ !!"
    else:
        return "Good Evening !!"

def home_page():
    st.markdown("""
        <style>

        /* Title styling */
        .title {
            font-size: 3.5rem;
            font-weight: 70;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }

        /* Info card styling */
        .info-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 1rem 0;
            transition: all 0.3s ease;
        }
        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }

        /* Text styling */
        .info-text {
            font-size: 1.2rem;
            color: #34495e;
            margin: 0.5rem 0;
        }
        .greeting {
            font-size: 3rem;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-top: 1.5rem;
        }
        
    
        </style>
    """, unsafe_allow_html=True)

    with st.spinner("Loading company information..."):
        time.sleep(1)
        data = get_company_data()

    if data:
        st.markdown(f"<h1 class='title'>{data['name']}</h1>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div class='info-card'>
                    <h3>🏢 Address</h3>
                    <p class='info-text'>{}</p>
                </div>
            """.format(data['address']), unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class='info-card'>
                    <h3>📧 Contact</h3>
                    <p class='info-text'>{}</p>
                </div>
            """.format(data['email']), unsafe_allow_html=True)

        st.write("")

        lottie_animation = load_lottie_file("assets/theatre.json")
        if lottie_animation:
            st_lottie(lottie_animation, height=200, key="welcome")

        greeting_message = get_greeting()
        st.markdown(f"<h2 class='greeting'>{greeting_message}</h2>", unsafe_allow_html=True)

        st.markdown("""
            <hr style='border: 1px solid #ddd; margin: 2rem 0;'>
            <p style='text-align: center; color: #666;'>
                © 2025 AMC Theatres | Powered by Streamlit
            </p>
        """, unsafe_allow_html=True)