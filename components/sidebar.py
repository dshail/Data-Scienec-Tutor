import streamlit as st
import os

def create_sidebar():
    """Render the sidebar with options and information"""
    with st.sidebar:
        st.image("static/images/logo.png", width=300)
        st.header("Data Science Tutor Settings (Development)")
        st.markdown("Customize your data science learning experience. Settings are currently under development.")
        st.markdown("---")
        
        # Render skill level selection
        skill_level = st.selectbox(
            "Your Skill Level",
            ["Beginner", "Intermediate", "Advanced"],
            help="Choose your data science proficiency level."
        )
        if "skill_level" not in st.session_state:
            st.session_state.skill_level = skill_level
        
        st.markdown("---")
        st.markdown("Powered by Gemini 1.5 Pro")
        st.markdown("Created by dshail")
        st.markdown("This application is in its early stages. Expect changes and improvements.")
        st.markdown("---")
        
        # Add GitHub link
        st.markdown("[GitHub](https://github.com/dshail/)")