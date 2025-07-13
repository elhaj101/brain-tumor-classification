import streamlit as st
import json
import os

def page_project_hypothesis_body():
    st.write("### Project Hypothesis")
    
    # Project overview
    st.write("#### Business Problem")
    st.write("""
    **Challenge:** Manual CT scan analysis for brain tumor detection is time-consuming, expensive, and subject to human error.
    
    **Opportunity:** Develop an automated system that can accurately detect brain tumors from CT scans, reducing costs and improving efficiency.
    """)
    
    # Hypothesis statement
    st.write("#### Hypothesis Statement")
    st.info("""
    **We believe that** a deep learning model can accurately classify brain CT scans as tumor or no-tumor with at least 85% accuracy.
    
    **This will achieve** significant cost savings (target: 85% cost reduction) and time savings (target: 87% time reduction) 
    compared to manual radiologist review.
    
    **We will know this to be true when** the model achieves our success criteria in production deployment.
    """)
    
    # Success criteria
    st.write("#### Success Criteria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Technical Metrics:**")
        st.write("✅ Model accuracy ≥ 85%")
        st.write("✅ Sensitivity (recall) ≥ 80%")
        st.write("✅ Specificity ≥ 80%")
        st.write("✅ F1-score ≥ 80%")
        st.write("✅ Inference time < 5 seconds")
    
    with col2:
        st.write("**Business Metrics:**")
        st.write("✅ Cost reduction ≥ 85%")
        st.write("✅ Time reduction ≥ 87%")
        st.write("✅ ROI > 500% annually")
        st.write("✅ User satisfaction ≥ 90%")
        st.write("✅ Deployment readiness")
    
    # Model validation results
    st.write("#### Hypothesis Validation Results")
    
    try:
        # Load evaluation metrics
        with open('evaluation_metrics.json', 'r') as f:
            metrics = json.load(f)
        
        # Load ROI configuration
        with open('roi_calculator_config.json', 'r') as f:
            roi_config = json.load(f)
        
        # Technical validation
        st.write("**Technical Performance:**")
        
        # Create metrics comparison
        technical_results = {
            'Accuracy': {
                'target': 0.85,
                'achieved': metrics.get('test_accuracy', 0),
                'status': '✅' if metrics.get('test_accuracy', 0) >= 0.85 else '❌'
            },
            'Sensitivity': {
                'target': 0.80,
                'achieved': metrics.get('optimal_sensitivity', 0),
                'status': '✅' if metrics.get('optimal_sensitivity', 0) >= 0.80 else '❌'
            },
            'Specificity': {
                'target': 0.80,
                'achieved': metrics.get('optimal_specificity', 0),
                'status': '✅' if metrics.get('optimal_specificity', 0) >= 0.80 else '❌'
            },
            'F1-Score': {
                'target': 0.80,
                'achieved': metrics.get('optimal_f1_score', 0),
                'status': '✅' if metrics.get('optimal_f1_score', 0) >= 0.80 else '❌'
            }
        }
        
        # Display technical results
        cols = st.columns(4)
        for i, (metric, data) in enumerate(technical_results.items()):
            with cols[i]:
                st.metric(
                    label=f"{metric} {data['status']}",
                    value=f"{data['achieved']:.1%}",
                    delta=f"Target: {data['target']:.1%}"
                )
        
        # Business validation
        st.write("**Business Impact:**")
        
        cost_params = roi_config['cost_params']
        cost_reduction = ((cost_params['manual_cost_per_scan'] - cost_params['automated_cost_per_scan']) / cost_params['manual_cost_per_scan']) * 100
        time_reduction = ((cost_params['radiologist_time_manual'] - cost_params['radiologist_time_automated']) / cost_params['radiologist_time_manual']) * 100
        
        # Calculate annual ROI for 10,000 scans
        annual_scans = 10000
        manual_cost = annual_scans * cost_params['manual_cost_per_scan']
        automated_cost = annual_scans * cost_params['automated_cost_per_scan']
        cost_savings = manual_cost - automated_cost
        roi_percentage = (cost_savings / automated_cost) * 100
        
        business_results = {
            'Cost Reduction': {
                'target': 85.0,
                'achieved': cost_reduction,
                'status': '✅' if cost_reduction >= 85.0 else '❌'
            },
            'Time Reduction': {
                'target': 87.0,
                'achieved': time_reduction,
                'status': '✅' if time_reduction >= 87.0 else '❌'
            },
            'Annual ROI': {
                'target': 500.0,
                'achieved': roi_percentage,
                'status': '✅' if roi_percentage >= 500.0 else '❌'
            }
        }
        
        # Display business results
        cols = st.columns(3)
        for i, (metric, data) in enumerate(business_results.items()):
            with cols[i]:
                unit = "%" if "ROI" in metric or "Reduction" in metric else ""
                st.metric(
                    label=f"{metric} {data['status']}",
                    value=f"{data['achieved']:.1f}{unit}",
                    delta=f"Target: {data['target']:.1f}{unit}"
                )
        
        # Overall hypothesis status
        st.write("#### Overall Hypothesis Status")
        
        # Check if hypothesis is validated
        technical_passed = all(result['status'] == '✅' for result in technical_results.values())
        business_passed = all(result['status'] == '✅' for result in business_results.values())
        
        if technical_passed and business_passed:
            st.success("🎉 **HYPOTHESIS VALIDATED!** All success criteria have been met.")
        elif technical_passed:
            st.warning("⚠️ **PARTIALLY VALIDATED:** Technical criteria met, business criteria need improvement.")
        elif business_passed:
            st.warning("⚠️ **PARTIALLY VALIDATED:** Business criteria met, technical criteria need improvement.")
        else:
            st.error("❌ **HYPOTHESIS NOT VALIDATED:** Multiple criteria need improvement.")
        
        # Detailed insights
        st.write("#### Key Insights")
        
        insights = []
        
        # Technical insights
        if metrics.get('test_accuracy', 0) >= 0.85:
            insights.append("✅ **High Accuracy:** Model exceeds minimum accuracy requirements")
        else:
            insights.append("⚠️ **Accuracy Concern:** Model accuracy below target - consider more training data")
        
        if cost_reduction >= 85.0:
            insights.append("✅ **Significant Cost Savings:** Automation reduces costs by over 85%")
        else:
            insights.append("⚠️ **Cost Optimization:** Cost reduction below target - review pricing model")
        
        if roi_percentage >= 500.0:
            insights.append("✅ **Strong ROI:** Annual return on investment exceeds 500%")
        else:
            insights.append("⚠️ **ROI Improvement:** ROI below target - scale deployment for better returns")
        
        for insight in insights:
            st.write(insight)
        
    except FileNotFoundError as e:
        st.error(f"❌ Cannot validate hypothesis - missing file: {e}")
        st.info("Please run ModelingAndEvaluating and DataVisualization notebooks first.")
    
    except Exception as e:
        st.error(f"❌ Error loading validation data: {e}")
    
    # Next steps
    st.write("#### Next Steps")
    
    st.write("**Immediate Actions:**")
    st.write("1. **Deploy to Production:** Set up automated CT scan processing pipeline")
    st.write("2. **User Training:** Train medical staff on the new system")
    st.write("3. **Monitor Performance:** Track real-world accuracy and user satisfaction")
    st.write("4. **Continuous Improvement:** Collect feedback and retrain model as needed")
    
    st.write("**Future Enhancements:**")
    st.write("- Expand to other imaging modalities (MRI, X-ray)")
    st.write("- Add tumor type classification (glioma, meningioma, pituitary)")
    st.write("- Implement explainable AI for radiologist confidence")
    st.write("- Integration with hospital information systems")
    
    # Risk assessment
    st.write("#### Risk Assessment")
    
    with st.expander("📋 View Risk Analysis"):
        st.write("**Technical Risks:**")
        st.write("- Model performance degradation with new data")
        st.write("- False positive/negative implications")
        st.write("- System integration challenges")
        
        st.write("**Business Risks:**")
        st.write("- Regulatory compliance requirements")
        st.write("- User adoption resistance")
        st.write("- Competition from established solutions")
        
        st.write("**Mitigation Strategies:**")
        st.write("- Continuous model monitoring and retraining")
        st.write("- Comprehensive user training programs")
        st.write("- Regular performance audits")
        st.write("- Backup manual review processes")