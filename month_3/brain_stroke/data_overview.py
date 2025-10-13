import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def add_engineered_features(df):
    """إضافة الميزات المحسنة إلى الداتا"""
    # Age groups with descriptive English labels
    bins_age = [0, 12, 18, 35, 50, 100]
    labels_age = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
    df['age_group'] = pd.cut(df['age'], bins=bins_age, labels=labels_age)
    
    # BMI categories
    bins_bmi = [0, 18.5, 24.9, 29.9, 100]
    labels_bmi = ['Underweight', 'Normal', 'Overweight', 'Obese']
    df['bmi_category'] = pd.cut(df['bmi'], bins=bins_bmi, labels=labels_bmi)
    
    # Glucose level categories
    bins_glucose = [0, 140, 199, 500]
    labels_glucose = ['Normal', 'Prediabetes', 'Diabetes']
    df['glucose_category'] = pd.cut(df['avg_glucose_level'], bins=bins_glucose, labels=labels_glucose)
    
    # حساب risk score (مؤشر خطر بسيط)
    df['risk_score'] = df['hypertension'] + df['heart_disease'] + (df['smoking_status'] == 'smokes').astype(int)
    
    return df

def show_data_overview_page(df):
    st.markdown('<div class="sub-header">📊 DATASET OVERVIEW</div>', unsafe_allow_html=True)
    
    if df is None:
        st.error("❌ No data available.")
        return

    # إضافة الميزات المحسنة
    df = add_engineered_features(df)
    
    # Calculate total features at the beginning
    total_features = len(df.columns)
    
    # Dropdown for section selection
    sections = [
        "📈 Basic Metrics", 
        "👀 Data Preview", 
        "🔍 Data Types & Summary", 
        "📉 Missing Values Analysis",
        "📊 Stroke Distribution"
    ]
    
    selected_section = st.selectbox(
        "🎯 Select Section to Explore:",
        sections,
        index=0
    )

    # Basic metrics section
    if selected_section == "📈 Basic Metrics":
        st.markdown("#### 📈 Dataset Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Patients", f"{len(df):,}")
        with col2:
            stroke_count = df['stroke'].sum()
            st.metric("Stroke Cases", f"{stroke_count:,}")
        with col3:
            stroke_rate = df['stroke'].mean() * 100
            st.metric("Stroke Rate", f"{stroke_rate:.2f}%")
        with col4:
            st.metric("Total Features", f"{total_features}")

        # Additional metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Original Features", "12")
        with col2:
            st.metric("Engineered Features", "4")  # age_group, bmi_category, glucose_category, risk_score
        with col3:
            numeric_features = len(df.select_dtypes(include=[np.number]).columns)
            st.metric("Numeric Features", f"{numeric_features}")
        with col4:
            categorical_features = len(df.select_dtypes(include=['object', 'category']).columns)
            st.metric("Categorical Features", f"{categorical_features}")

    # Data preview section
    elif selected_section == "👀 Data Preview":
        st.markdown("#### 👀 Data Preview")
        
        # Show data dimensions
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Dataset Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
        with col2:
            st.info(f"**Memory Usage:** {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        # Data preview with options
        preview_option = st.radio(
            "Show:",
            ["First 10 Rows", "Last 10 Rows", "Random 10 Rows"],
            horizontal=True
        )
        
        if preview_option == "First 10 Rows":
            st.dataframe(df.head(10), use_container_width=True)
        elif preview_option == "Last 10 Rows":
            st.dataframe(df.tail(10), use_container_width=True)
        else:
            st.dataframe(df.sample(10), use_container_width=True)

    # Data types and summary section
    elif selected_section == "🔍 Data Types & Summary":
        st.markdown("#### 🔍 Data Structure Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📋 Data Types")
            dtypes_df = pd.DataFrame({
                'Column': df.columns,
                'Data Type': df.dtypes,
                'Non-Null Count': df.notnull().sum()
            })
            st.dataframe(dtypes_df, use_container_width=True)
            
        with col2:
            st.markdown("##### 🔢 Numerical Summary")
            numerical_cols = df.select_dtypes(include=[np.number]).columns
            if len(numerical_cols) > 0:
                st.dataframe(df[numerical_cols].describe(), use_container_width=True)
            else:
                st.warning("No numerical columns found.")

    # Missing values analysis section
    elif selected_section == "📉 Missing Values Analysis":
        st.markdown("#### 📉 Missing Values Analysis")
        
        # Create missing values dataframe for all features
        missing_df = pd.DataFrame({
            'Column': df.columns,
            'Missing Count': df.isnull().sum(),
            'Missing Percentage': (df.isnull().sum() / len(df)) * 100
        }).sort_values('Missing Count', ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Missing Values Table")
            st.dataframe(missing_df, use_container_width=True)
            
        with col2:
            st.markdown("##### 📈 Missing Values Visualization")
            
            # Create bar chart for missing values
            if missing_df['Missing Count'].sum() > 0:
                fig = px.bar(
                    missing_df[missing_df['Missing Count'] > 0],
                    x='Column',
                    y='Missing Count',
                    title='Missing Values by Column',
                    color='Missing Count',
                    color_continuous_scale='reds'
                )
                fig.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.success("🎉 No missing values found in the dataset!")

    # Stroke distribution section
    elif selected_section == "📊 Stroke Distribution":
        st.markdown("#### 📊 Stroke Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Stroke Distribution")
            stroke_counts = df['stroke'].value_counts().sort_index()
            labels = ['No Stroke (0)', 'Stroke (1)']
            values = [stroke_counts.get(0, 0), stroke_counts.get(1, 0)]
            
            # Updated colors to pink and light purple
            fig_pie = px.pie(
                values=values, 
                names=labels,
                color_discrete_sequence=['#FFB6C1', '#D8BFD8'],  # Light Pink and Light Purple
                title='Stroke vs No Stroke Distribution'
            )
            # Customize the pie chart further
            fig_pie.update_traces(
                textinfo='percent+label',
                marker=dict(line=dict(color='#000000', width=1))
            )
            fig_pie.update_layout(
                font=dict(size=14),
                showlegend=True
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with col2:
            st.markdown("##### 📊 Stroke Statistics")
            
            # Stroke statistics
            total_cases = len(df)
            stroke_cases = stroke_counts.get(1, 0)
            no_stroke_cases = stroke_counts.get(0, 0)
            
            st.metric("Total Cases", f"{total_cases:,}")
            st.metric("Stroke Cases", f"{stroke_cases:,}")
            st.metric("No Stroke Cases", f"{no_stroke_cases:,}")
            st.metric("Stroke Prevalence", f"{(stroke_cases/total_cases)*100:.2f}%")
            
            # Additional info
            st.markdown("##### ℹ️ Dataset Info")
            st.info(f"""
            - **Original Features:** 12
            - **Engineered Features:** 4 (age_group, bmi_category, glucose_category, risk_score)
            - **Total Features:** {total_features}
            - **Dataset Balance:** {'Imbalanced' if stroke_cases/total_cases < 0.1 else 'Balanced'}
            """)

    # Quick summary at the bottom
    st.markdown("---")
    st.markdown("### 🎯 Quick Dataset Summary")
    
    summary_col1, summary_col2, summary_col3 = st.columns(3)
    
    with summary_col1:
        st.markdown("**📊 Dimensions**")
        st.write(f"• Rows: {df.shape[0]:,}")
        st.write(f"• Columns: {df.shape[1]}")
        st.write(f"• Total Values: {df.shape[0] * df.shape[1]:,}")
        
    with summary_col2:
        st.markdown("**🔧 Data Types**")
        numeric_count = len(df.select_dtypes(include=[np.number]).columns)
        categorical_count = len(df.select_dtypes(include=['object', 'category']).columns)
        st.write(f"• Numerical: {numeric_count}")
        st.write(f"• Categorical: {categorical_count}")
        
    with summary_col3:
        st.markdown("**📈 Health Metrics**")
        st.write(f"• Stroke Cases: {df['stroke'].sum():,}")
        st.write(f"• Stroke Rate: {df['stroke'].mean()*100:.2f}%")
        st.write(f"• Complete Cases: {df.isnull().sum().sum() == 0}")