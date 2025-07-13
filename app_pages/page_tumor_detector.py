import streamlit as st
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import os

def preprocess_image(image, target_size=(224, 224)):
    """Preprocess image for model prediction"""
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize to target size
    image = image.resize(target_size)
    
    # Convert to numpy array and normalize
    img_array = np.array(image)
    img_array = img_array.astype(np.float32) / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def page_tumor_detector_body():
    st.write("### Brain Tumor Detection")
    
    # Load sample images
    try:
        with open('image_samples.json', 'r') as f:
            image_samples = json.load(f)
        
        # Sample images section
        st.write("#### Sample Images by Class")
        class_choice = st.selectbox("Select Class", ['tumor', 'notumor'])
        
        if class_choice == 'tumor':
            sample_paths = image_samples['tumor_paths']
        else:
            sample_paths = image_samples['notumor_paths']
        
        # Display sample images in grid
        cols = st.columns(3)
        for i, img_path in enumerate(sample_paths[:6]):
            with cols[i % 3]:
                try:
                    if os.path.exists(img_path):
                        img = Image.open(img_path)
                        st.image(img, caption=f"Sample {i+1}", use_column_width=True)
                    else:
                        st.warning(f"Image not found: {os.path.basename(img_path)}")
                except Exception as e:
                    st.error(f"Could not load {os.path.basename(img_path)}: {e}")
    
        # File upload section
        st.write("#### Upload CT Scan for Prediction")
        uploaded_file = st.file_uploader("Choose a CT scan image", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file is not None:
            # Load and display image
            image = Image.open(uploaded_file)
            
            # Display image in columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(image, caption="Uploaded CT Scan", use_column_width=True)
            
            with col2:
                # Load model and make prediction
                if st.button("🔍 Predict Tumor", type="primary"):
                    try:
                        # Show loading spinner
                        with st.spinner('Loading model and making prediction...'):
                            # Load model
                            if os.path.exists('best_brain_tumor_model.keras'):
                                model = tf.keras.models.load_model('best_brain_tumor_model.keras')
                                
                                # Preprocess image
                                processed_image = preprocess_image(image)
                                
                                # Make prediction
                                prediction = model.predict(processed_image, verbose=0)
                                confidence = float(prediction[0][0])
                                
                                # Interpret results
                                if confidence > 0.5:
                                    result = "TUMOR DETECTED"
                                    probability = confidence
                                    color = "red"
                                    emoji = "🚨"
                                else:
                                    result = "NO TUMOR DETECTED"
                                    probability = 1 - confidence
                                    color = "green"
                                    emoji = "✅"
                                
                                # Display results
                                st.markdown(f"### {emoji} {result}")
                                st.markdown(f"**Confidence:** {probability:.1%}")
                                
                                # Progress bar for confidence
                                st.progress(probability)
                                
                                # Additional info
                                st.info(f"Raw prediction score: {confidence:.4f}")
                                
                                # Recommendations
                                if confidence > 0.5:
                                    st.warning("⚠️ **Recommendation:** Consult with a radiologist for further evaluation.")
                                else:
                                    st.success("✅ **Result:** No immediate concerns detected.")
                                
                            else:
                                st.error("❌ Model file not found. Please run ModelingAndEvaluating notebook first.")
                                
                    except Exception as e:
                        st.error(f"❌ Prediction error: {e}")
                        st.info("Make sure the model file exists and is properly trained.")
                
                # Model information
                st.write("#### Model Information")
                try:
                    # Load evaluation metrics if available
                    if os.path.exists('evaluation_metrics.json'):
                        with open('evaluation_metrics.json', 'r') as f:
                            metrics = json.load(f)
                        
                        st.write(f"**Accuracy:** {metrics.get('test_accuracy', 'N/A'):.1%}")
                        st.write(f"**Sensitivity:** {metrics.get('optimal_sensitivity', 'N/A'):.1%}")
                        st.write(f"**Specificity:** {metrics.get('optimal_specificity', 'N/A'):.1%}")
                    else:
                        st.write("Model metrics not available")
                except:
                    st.write("Model metrics not available")
                    
    except FileNotFoundError:
        st.error("❌ Sample images not found. Please run DataVisualization notebook first.")
        st.info("Required files: image_samples.json")
    
    # Additional information section
    st.write("---")
    st.write("#### About This Tool")
    st.write("""
    This brain tumor detection tool uses a deep learning model trained on CT scan images to identify potential tumors.
    
    **Important Notes:**
    - This tool is for educational/research purposes only
    - Results should not be used for medical diagnosis
    - Always consult with qualified medical professionals
    - The model achieves ~90% accuracy on test data
    """)
    
    # Usage instructions
    with st.expander("📋 How to Use"):
        st.write("""
        1. **View Samples:** Select 'tumor' or 'notumor' to see example images
        2. **Upload Image:** Choose a CT scan image (PNG, JPG, or JPEG)
        3. **Get Prediction:** Click 'Predict Tumor' to analyze the image
        4. **Interpret Results:** Review the confidence score and recommendations
        """)

        # Test script
import sys
sys.path.append('/workspaces/brain-tumor-classification')

from app_pages.page_tumor_detector import preprocess_image
from PIL import Image
import numpy as np

