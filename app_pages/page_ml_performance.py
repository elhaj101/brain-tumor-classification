import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import your dashboard functions
import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def page_ml_performance_body():
    st.write("### ML Performance Dashboard")
    
    # Load artifacts
    try:
        with open('evaluation_metrics.json', 'r') as f:
            metrics = json.load(f)
        
        with open('confusion_matrices.json', 'r') as f:
            confusion_data = json.load(f)
            
        df_predictions = pd.read_csv('test_predictions.csv')
        
        # Create performance visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("#### Confusion Matrix")
            # Add confusion matrix heatmap
            
        with col2:
            st.write("#### Performance Metrics")
            # Add metrics bar chart
            
        # Confidence distribution
        st.write("#### Confidence Score Distribution")
        # Add confidence histogram
        
    except FileNotFoundError as e:
        st.error(f"Missing file: {e}")
        st.info("Please run DataVisualization notebook first")