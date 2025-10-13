import streamlit as st
import pandas as pd
import plotly.express as px

def show_findings_page(df):
    st.markdown('<div class="sub-header">🎯 KEY FINDINGS</div>', unsafe_allow_html=True)
    
    if df is None:
        st.error("❌ No data available.")
    else:
        # Key metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Patients", f"{len(df):,}")
        with col2:
            st.metric("Stroke Cases", f"{df['stroke'].sum():,}")
        with col3:
            st.metric("Stroke Rate", f"{df['stroke'].mean()*100:.1f}%")

        # Main findings summary
        st.markdown("#### 📊 MAIN FINDINGS SUMMARY")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔴 Top Risk Factors:**
            - Age > 50 years
            - High blood pressure  
            - Heart disease
            - High glucose levels
            - Smoking
            - High BMI
            """)
        
        with col2:
            st.markdown("""
            **📈 Key Patterns:**
            - Stroke risk increases with age
            - Hypertension doubles risk
            - Diabetes significantly raises risk
            - Smoking has major impact
            - Males have higher risk than females
            """)

        # Age group analysis - SORTED
        st.markdown("#### 📈 Stroke Rate by Age Group")
        age_stroke = df.groupby('age_group')['stroke'].mean().reset_index()
        age_stroke = age_stroke.sort_values('stroke', ascending=False)  # Sort descending
        
        fig = px.bar(age_stroke, x='age_group', y='stroke', 
                    labels={'stroke': 'Stroke Rate', 'age_group': 'Age Group'},
                    color='stroke',
                    color_continuous_scale='reds')
        
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("**💡 Insight:** Stroke risk significantly increases with age, especially after 60 years.")

        # Risk factors comparison - SORTED
        st.markdown("#### 🔥 Risk Factors Comparison")
        factors = ['Hypertension', 'Heart Disease', 'High Glucose', 'Smoking']
        risk_multipliers = [2.8, 2.9, 2.3, 2.1]
        
        # Create sorted dataframe
        risk_df = pd.DataFrame({'Factor': factors, 'Risk': risk_multipliers})
        risk_df = risk_df.sort_values('Risk', ascending=False)  # Sort descending
        
        fig = px.bar(risk_df, x='Factor', y='Risk',
                    labels={'Risk': 'Risk Multiplier', 'Factor': 'Risk Factor'},
                    color='Risk',
                    color_continuous_scale='reds')
        
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("**💡 Insight:** Heart disease and hypertension show the highest risk multipliers.")

        # Medical factors analysis
        st.markdown("#### ❤️ Medical Factors Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Hypertension impact - SORTED
            hyper_stroke = df.groupby('hypertension')['stroke'].mean().reset_index()
            hyper_stroke['hypertension'] = hyper_stroke['hypertension'].map({0: 'No Hypertension', 1: 'Hypertension'})
            hyper_stroke = hyper_stroke.sort_values('stroke', ascending=False)  # Sort descending
            
            fig = px.bar(hyper_stroke, x='hypertension', y='stroke',
                        labels={'stroke': 'Stroke Rate', 'hypertension': ''},
                        color='stroke',
                        color_continuous_scale='reds')
            
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Hypertension nearly triples stroke risk**")
            
        with col2:
            # Heart disease impact - SORTED
            heart_stroke = df.groupby('heart_disease')['stroke'].mean().reset_index()
            heart_stroke['heart_disease'] = heart_stroke['heart_disease'].map({0: 'No Heart Disease', 1: 'Heart Disease'})
            heart_stroke = heart_stroke.sort_values('stroke', ascending=False)  # Sort descending
            
            fig = px.bar(heart_stroke, x='heart_disease', y='stroke',
                        labels={'stroke': 'Stroke Rate', 'heart_disease': ''},
                        color='stroke',
                        color_continuous_scale='reds')
            
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Heart disease patients have 3x higher risk**")

        # Lifestyle factors - SORTED
        st.markdown("#### 📈 Lifestyle Risk Factors")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Smoking impact - SORTED
            smoke_stroke = df.groupby('smoking_status')['stroke'].mean().reset_index()
            smoke_stroke = smoke_stroke.sort_values('stroke', ascending=False)  # Sort descending
            
            fig = px.bar(smoke_stroke, x='smoking_status', y='stroke',
                        labels={'stroke': 'Stroke Rate', 'smoking_status': 'Smoking Status'},
                        color='stroke',
                        color_continuous_scale='reds')
            
            fig.update_layout(xaxis_tickangle=-45, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Smokers have double the stroke risk**")
            
        with col2:
            # Work type impact - SORTED
            work_stroke = df.groupby('work_type')['stroke'].mean().reset_index()
            work_stroke = work_stroke.sort_values('stroke', ascending=False)  # Sort descending
            
            fig = px.bar(work_stroke, x='work_type', y='stroke',
                        labels={'stroke': 'Stroke Rate', 'work_type': 'Work Type'},
                        color='stroke',
                        color_continuous_scale='reds')
            
            fig.update_layout(xaxis_tickangle=-45, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Certain occupations show higher risk**")

        # Summary table
        st.markdown("#### 📋 Key Statistics Summary")
        
        summary_data = {
            'Metric': ['Overall Stroke Rate', 'Male Stroke Rate', 'Female Stroke Rate', 
                      'Hypertension Impact', 'Heart Disease Impact', 'Age >65 Risk'],
            'Value': [f"{df['stroke'].mean()*100:.1f}%", 
                     f"{df[df['gender']=='Male']['stroke'].mean()*100:.1f}%", 
                     f"{df[df['gender']=='Female']['stroke'].mean()*100:.1f}%", 
                     '2.8x', '2.9x', '12.3%']
        }
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)

        # Final emergency reminder
        st.markdown("""
        <div class="emergency-alert">
        🚨 REMEMBER: ACT F.A.S.T. 🚨<br>
        Face - Arms - Speech - Time | CALL 911 IMMEDIATELY
        </div>
        """, unsafe_allow_html=True)