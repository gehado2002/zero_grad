import streamlit as st
import pandas as pd
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

def show_analysis_page(df):
    st.markdown('<div class="sub-header">📈 DATA ANALYSIS</div>', unsafe_allow_html=True)
    
    if df is None:
        st.error("❌ No data available.")
        return
    
    # إضافة الميزات المحسنة للتأكد من وجودها
    df = add_engineered_features(df)
    
    tab1, tab2 = st.tabs(["📊 Feature Analysis", "🔗 Relationships"])
    
    with tab1:
        st.markdown("#### Feature Distributions")
        
        analysis_type = st.radio("Select Analysis Type:", ["Numerical", "Categorical", "Trend Analysis"])
        
        if analysis_type == "Numerical":
            # جميع الأعمدة الرقمية المتاحة
            num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            
            # إزالة الأعمدة غير المرغوبة فقط
            columns_to_exclude = ['id']
            num_cols = [col for col in num_cols if col not in columns_to_exclude]
            
            # إضافة الأعمدة الناقصة إذا لم تكن موجودة
            essential_num_cols = ['age', 'avg_glucose_level', 'bmi', 'hypertension', 'heart_disease', 'risk_score', 'stroke']
            for col in essential_num_cols:
                if col in df.columns and col not in num_cols:
                    num_cols.append(col)
            
            # ترتيب الأعمدة بشكل منطقي
            preferred_order = ['age', 'avg_glucose_level', 'bmi', 'hypertension', 'heart_disease', 'risk_score', 'stroke']
            num_cols_sorted = []
            
            # إضافة الأعمدة المفضلة أولاً
            for col in preferred_order:
                if col in num_cols:
                    num_cols_sorted.append(col)
                    num_cols.remove(col)
            
            # إضافة باقي الأعمدة
            num_cols_sorted.extend(sorted(num_cols))
            
            if not num_cols_sorted:
                st.warning("No numerical columns available for analysis.")
            else:
                selected_num = st.selectbox("Select Feature:", num_cols_sorted)
                
                fig = px.histogram(df, x=selected_num, nbins=30,
                                 title=f'Distribution of {selected_num}',
                                 color_discrete_sequence=['#1f77b4'],
                                 opacity=0.8)
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='black')
                )
                st.plotly_chart(fig, use_container_width=True)
                    
        elif analysis_type == "Categorical":
            # جميع الأعمدة الفئوية المتاحة
            cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
            
            # إضافة الأعمدة الفئوية من النوع الرقمي إذا كانت موجودة
            additional_cat_cols = ['age_group', 'bmi_category', 'glucose_category', 'gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
            for col in additional_cat_cols:
                if col in df.columns and col not in cat_cols:
                    cat_cols.append(col)
            
            # ترتيب الأعمدة الفئوية
            preferred_cat_order = ['gender', 'age_group', 'work_type', 'smoking_status', 'bmi_category', 'glucose_category', 'ever_married', 'Residence_type']
            cat_cols_sorted = []
            
            for col in preferred_cat_order:
                if col in cat_cols:
                    cat_cols_sorted.append(col)
                    cat_cols.remove(col)
            
            cat_cols_sorted.extend(sorted(cat_cols))
            
            if not cat_cols_sorted:
                st.warning("No categorical columns available for analysis.")
            else:
                selected_cat = st.selectbox("Select Feature:", cat_cols_sorted)
                
                value_counts = df[selected_cat].value_counts()
                fig = px.bar(x=value_counts.index, y=value_counts.values,
                            title=f'Distribution of {selected_cat}',
                            labels={'x': selected_cat, 'y': 'Count'},
                            color=value_counts.values,
                            color_continuous_scale='blues')
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='black')
                )
                st.plotly_chart(fig, use_container_width=True)
        
        else:  # Trend Analysis
            st.markdown("##### Trend Analysis Over Age")
            
            # اختيار المتغير للتحليل
            trend_vars = ['avg_glucose_level', 'bmi', 'hypertension', 'heart_disease']
            selected_trend = st.selectbox("Select Variable to Analyze:", trend_vars)
            
            # إنشاء age bins للتحليل
            df_age_groups = df.copy()
            df_age_groups['age_bin'] = pd.cut(df_age_groups['age'], bins=range(0, 101, 10))
            
            # حساب المتوسط حسب الفئة العمرية
            trend_data = df_age_groups.groupby('age_bin')[selected_trend].mean().reset_index()
            trend_data['age_bin'] = trend_data['age_bin'].astype(str)
            
            # إنشاء الـ line plot
            fig = px.line(trend_data, x='age_bin', y=selected_trend,
                         title=f'{selected_trend} Trend by Age Group',
                         markers=True,
                         line_shape='linear')
            fig.update_layout(
                xaxis_title='Age Group',
                yaxis_title=f'Average {selected_trend}',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='black')
            )
            fig.update_traces(line=dict(color='#1f77b4', width=3))
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("#### Feature Relationships")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # جميع الأعمدة الرقمية للعلاقات
            num_cols_relation = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            
            # إزالة الأعمدة غير المرغوبة فقط
            num_cols_relation = [col for col in num_cols_relation if col not in ['id']]
            
            # إضافة الأعمدة الناقصة
            essential_relation_cols = ['age', 'avg_glucose_level', 'bmi', 'hypertension', 'heart_disease', 'risk_score', 'stroke']
            for col in essential_relation_cols:
                if col in df.columns and col not in num_cols_relation:
                    num_cols_relation.append(col)
            
            # ترتيب الأعمدة
            preferred_relation_order = ['age', 'avg_glucose_level', 'bmi', 'hypertension', 'heart_disease', 'risk_score', 'stroke']
            num_cols_relation_sorted = []
            
            for col in preferred_relation_order:
                if col in num_cols_relation:
                    num_cols_relation_sorted.append(col)
                    num_cols_relation.remove(col)
            
            num_cols_relation_sorted.extend(sorted(num_cols_relation))
            
            x_axis = st.selectbox("X Axis:", num_cols_relation_sorted, index=0)
        
        with col2:
            y_axis = st.selectbox("Y Axis:", num_cols_relation_sorted, index=min(1, len(num_cols_relation_sorted)-1))
        
        with col3:
            color_by = st.selectbox("Color by:", ['None', 'stroke', 'gender', 'age_group', 'bmi_category', 'smoking_status'])
        
        # إعداد ألوان مناسبة للوضع النهاري
        if color_by == 'None':
            fig = px.scatter(df, x=x_axis, y=y_axis,
                           title=f'{x_axis} vs {y_axis}',
                           opacity=0.7,
                           color_discrete_sequence=['#1f77b4'])
        else:
            color_map = {
                'stroke': {0: '#1f77b4', 1: '#ff7f0e'},  # أزرق وبرتقالي
                'gender': {'Male': '#1f77b4', 'Female': '#ff7f0e', 'Other': '#2ca02c'},
                'smoking_status': {'never smoked': '#1f77b4', 'formerly smoked': '#ff7f0e', 'smokes': '#d62728', 'Unknown': '#7f7f7f'}
            }
            
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_by,
                           title=f'{x_axis} vs {y_axis} by {color_by}',
                           opacity=0.7,
                           color_discrete_map=color_map.get(color_by, None),
                           hover_data=['age', 'gender', 'bmi_category'])
        
        # تحسين التصميم للوضع النهاري
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='black'),
            legend=dict(
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='black',
                borderwidth=1
            )
        )
        
        # إضافة خط الاتجاه
        if len(df) > 1:  # التأكد من وجود بيانات كافية
            fig.add_traces(px.scatter(df, x=x_axis, y=y_axis, trendline="ols").data[1])
        
        st.plotly_chart(fig, use_container_width=True)