import streamlit as st
import json
from PIL import Image
import os

def page_visualizer_body():
    st.write("### Interactive Image Explorer")
    
    try:
        with open('image_samples.json', 'r') as f:
            image_samples = json.load(f)
        
        # Interactive class selection
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.write("#### Controls")
            selected_class = st.radio("Select Class", ['tumor', 'notumor'])
            num_samples = st.slider("Number of Samples", 1, 6, 6)
        
        with col2:
            st.write(f"#### {selected_class.title()} Samples")
            
            if selected_class == 'tumor':
                sample_paths = image_samples['tumor_paths'][:num_samples]
            else:
                sample_paths = image_samples['notumor_paths'][:num_samples]
            
            # Display images in grid
            cols = st.columns(3)
            for i, img_path in enumerate(sample_paths):
                with cols[i % 3]:
                    if os.path.exists(img_path):
                        img = Image.open(img_path)
                        st.image(img, caption=f"Sample {i+1}", use_column_width=True)
                    else:
                        st.error(f"Image not found: {img_path}")
    
    except FileNotFoundError:
        st.error("Image samples not found. Please run DataVisualization notebook first.")