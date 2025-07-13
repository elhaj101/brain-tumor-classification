import streamlit as st
from app_pages.multipage import MultiPage

# Import your app pages
from app_pages import (
    page_summary,
    page_project_hypothesis,
    page_tumor_detector,
    page_visualizer,
    page_ml_performance
)

# Create MultiPage instance
app = MultiPage()

# Set up the main page
st.set_page_config(
    page_title="Brain Tumor Classification Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add title and description
st.title("🧠 Brain Tumor Classification Dashboard")
st.markdown("---")

# Add pages to the app
app.add_page("Quick Project Summary", page_summary.page_summary_body)
app.add_page("Project Hypothesis", page_project_hypothesis.page_project_hypothesis_body)
app.add_page("Tumor Detector", page_tumor_detector.page_tumor_detector_body)
app.add_page("Image Visualizer", page_visualizer.page_visualizer_body)
app.add_page("ML Performance Metrics", page_ml_performance.page_ml_performance_body)

# Run the app
app.run()