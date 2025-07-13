import streamlit as st
import json
import plotly.graph_objects as go

def page_summary_body():
    st.write("### Project Summary & Business Value")
    
    try:
        # Load evaluation metrics
        with open('evaluation_metrics.json', 'r') as f:
            metrics = json.load(f)
        
        # Load ROI config
        with open('roi_calculator_config.json', 'r') as f:
            roi_config = json.load(f)
        
        # Model Performance Summary
        st.write("#### Model Performance")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Accuracy", f"{metrics['test_accuracy']:.1%}")
        with col2:
            st.metric("Sensitivity", f"{metrics['optimal_sensitivity']:.1%}")
        with col3:
            st.metric("Specificity", f"{metrics['optimal_specificity']:.1%}")
        with col4:
            st.metric("F1-Score", f"{metrics['optimal_f1_score']:.1%}")
        
        # ROI Calculator
        st.write("#### ROI Calculator")
        num_scans = st.slider("Number of CT Scans per Year", 100, 50000, 10000)
        
        # Calculate ROI
        cost_params = roi_config['cost_params']
        manual_cost = num_scans * cost_params['manual_cost_per_scan']
        automated_cost = num_scans * cost_params['automated_cost_per_scan']
        cost_savings = manual_cost - automated_cost
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Annual Cost Savings", f"${cost_savings:,.0f}")
        with col2:
            st.metric("Cost per Scan Reduction", f"{((cost_params['manual_cost_per_scan'] - cost_params['automated_cost_per_scan']) / cost_params['manual_cost_per_scan'] * 100):.1f}%")
        with col3:
            st.metric("ROI", f"{(cost_savings / automated_cost * 100):.1f}%")
        
    except FileNotFoundError as e:
        st.error(f"Missing configuration file: {e}")