"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Credit Card Fraud Detection")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Credit Card Fraud is predicting which customers are at high risk of leaving your company or canceling a subscription to a service, based on their behavior with your product.
        </p>
    """, unsafe_allow_html=True)