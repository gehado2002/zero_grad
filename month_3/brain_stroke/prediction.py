import streamlit as st
import plotly.graph_objects as go

def show_prediction_page():
    st.markdown("## 🤖 Stroke Risk Prediction")
    
    # Medical Disclaimer
    st.warning("⚠️ **Note**: This tool is for educational purposes only. Consult doctors for medical advice.")
    
    # Patient Form
    st.markdown("### 📝 Patient Information")
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider("Age", 1, 100, 50)
            hypertension = st.selectbox("Hypertension", ["No", "Yes"])
            smoking_status = st.selectbox("Smoking", ["Never", "Former", "Current"])
            avg_glucose_level = st.slider("Glucose Level", 50, 300, 120)
            
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
            bmi = st.slider("BMI", 15.0, 50.0, 25.0, 0.1)
            work_type = st.selectbox("Work Type", ["Private", "Government", "Self-employed", "Never worked"])
        
        submitted = st.form_submit_button("🔍 Predict Risk", use_container_width=True)

    # Real-time Risk Calculation
    st.markdown("### ⚡ Risk Assessment")
    
    risk_score = 0
    risk_factors = []
    
    # Calculate risk
    if age >= 65: risk_score += 3; risk_factors.append("Age 65+")
    elif age >= 50: risk_score += 2; risk_factors.append("Age 50-64")
    
    if hypertension == "Yes": risk_score += 3; risk_factors.append("Hypertension")
    if heart_disease == "Yes": risk_score += 3; risk_factors.append("Heart Disease")
    if smoking_status == "Current": risk_score += 2; risk_factors.append("Smoking")
    if avg_glucose_level > 140: risk_score += 1; risk_factors.append("High Glucose")
    if bmi >= 30: risk_score += 2; risk_factors.append("Obesity")
    elif bmi >= 25: risk_score += 1; risk_factors.append("Overweight")

    # Display Risk Level
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if risk_score >= 8:
            st.error("🔴 HIGH RISK")
            prob = "15-30%"
        elif risk_score >= 5:
            st.warning("🟡 MEDIUM RISK")
            prob = "5-15%"
        else:
            st.success("🟢 LOW RISK")
            prob = "1-5%"
    
    with col2:
        st.metric("Risk Score", risk_score)
    
    with col3:
        st.metric("Probability", prob)

    # Risk Factors
    if risk_factors:
        st.markdown("**🚨 Risk Factors:**")
        cols = st.columns(3)
        for i, factor in enumerate(risk_factors):
            cols[i % 3].write(f"• {factor}")

    # Results after submission
    if submitted:
        st.markdown("---")
        st.success("**Analysis Complete**")
        
        # Simple probability calculation
        probability = min(2 + (age * 0.3) + (10 if hypertension=="Yes" else 0) + 
                         (10 if heart_disease=="Yes" else 0) + (5 if smoking_status=="Current" else 0), 40)
        
        # Results in columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Your Risk Level")
            st.progress(int(probability))
            st.write(f"**Estimated stroke probability: {probability:.1f}%**")
            
            if probability > 20:
                st.error("Consult doctor immediately")
            elif probability > 10:
                st.warning("Monitor your health regularly")
            else:
                st.success("Maintain healthy lifestyle")
        
        with col2:
            st.markdown("#### 💡 Recommendations")
            
            if hypertension == "Yes":
                st.write("• Monitor blood pressure daily")
            if heart_disease == "Yes":
                st.write("• Regular heart check-ups")
            if smoking_status == "Current":
                st.write("• Quit smoking program")
            if bmi >= 25:
                st.write("• Weight management")
            
            st.write("• Exercise 150 mins/week")
            st.write("• Healthy diet")
            st.write("• Annual health check-up")

        # Emergency Info
        st.markdown("---")
        st.markdown("#### 🚨 Emergency Signs - ACT F.A.S.T.")
        st.write("**F**ace drooping • **A**rm weakness • **S**peech difficulty • **T**ime to call 911")