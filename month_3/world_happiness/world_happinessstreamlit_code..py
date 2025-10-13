# world_happiness_dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from io import BytesIO
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------ Page Config ------------------
st.set_page_config(page_title="😊 World Happiness Dashboard", layout="wide")

# ------------------ Helpers ------------------
def guess_and_rename(df):
    col_map = {}
    lower_cols = {c.lower(): c for c in df.columns}

    # Country
    for key in ["country", "country name", "country_name", "nation"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Country"
            break
    # Region
    for key in ["region", "regional indicator", "region_name"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Region"
            break
    # Happiness
    for key in ["happiness", "score", "life ladder", "happiness_score", "ladder score"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Happiness"
            break
    # GDP (detect multiple variants)
    for key in ["gdp", "gdp per capita", "gdp_per_capita", "economy (gdp per capita)", "logged gdp per capita"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "GDP"
            break
    # Social support
    for key in ["social support", "social", "social_support"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Social_support"
            break
    # Life expectancy
    for key in ["life expectancy", "healthy life expectancy", "life_expectancy"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Life_expectancy"
            break
    # Freedom
    for key in ["freedom", "freedom to make life choices"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Freedom"
            break
    # Generosity
    if "generosity" in lower_cols:
        col_map[lower_cols["generosity"]] = "Generosity"
    # Corruption
    for key in ["corruption", "perceptions of corruption"]:
        if key in lower_cols:
            col_map[lower_cols[key]] = "Corruption"
            break

    df = df.rename(columns=col_map)
    return df

def load_data(uploaded_file=None):
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            return guess_and_rename(df)
        except:
            st.warning("Failed to load uploaded file. Loading default dataset.")
    default_path = r"world-happiness-report.csv"
    try:
        df = pd.read_csv(default_path)
        return guess_and_rename(df)
    except:
        st.error("Default dataset not found. Please upload a CSV/Excel file.")
        st.stop()

# ------------------ Load Data ------------------
uploaded = st.sidebar.file_uploader("Upload World Happiness CSV / Excel", type=["csv","xlsx","xls"])
df = load_data(uploaded)

# ------------------ Ensure numeric columns ------------------
numeric_cols = ["Happiness","GDP","Social_support","Life_expectancy","Freedom","Generosity","Corruption"]
for c in numeric_cols:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

# Create Log GDP column if GDP exists
if 'GDP' in df.columns:
    df['Log_GDP'] = np.log(df['GDP'].replace(0,np.nan))
    numeric_cols.append('Log_GDP')

# Handle missing Region column
if 'Region' not in df.columns:
    df['Region'] = 'Unknown'
else:
    df['Region'] = df['Region'].fillna('Unknown')

# ------------------ Initialize session state for page navigation ------------------
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# ------------------ Sidebar Filters ------------------
regions = sorted(df['Region'].dropna().unique().tolist())
countries = sorted(df['Country'].dropna().unique().tolist())

selected_regions = st.sidebar.multiselect("Select Region(s)", options=regions, default=regions)
compare_countries = st.sidebar.multiselect("Select 2–3 countries to compare", options=countries, default=countries[:2])
q_low = st.sidebar.slider("Low-income quantile cutoff", 0.05, 0.45, 0.33)
q_high = st.sidebar.slider("High-income quantile cutoff", 0.55, 0.95, 0.67)

# ------------------ Page Header ------------------
st.title("😊 World Happiness Dashboard")
st.image("https://ds8526jcpbygs.cloudfront.net/wp-content/uploads/2016/08/happysad.jpg", use_container_width=True)
st.markdown("""
📊 Source: [World Happiness Report on Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness)  
💻 Open in Google Colab: [Click Here](https://colab.research.google.com/drive/1d255zrcW8xCDlBhgW4_BtP7ELHDqvBP4?usp=sharing)
""")

# ------------------ Page Navigation Buttons ------------------
st.markdown("### Navigate Dashboard:")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 Home"): st.session_state.current_page = "Home"
with col2:
    if st.button("🔍 Insights"): st.session_state.current_page = "Insights"
with col3:
    if st.button("📊 Compare"): st.session_state.current_page = "Compare"
with col4:
    if st.button("📈 Summary"): st.session_state.current_page = "Summary"

# Optional CSS for button style
st.markdown("""
<style>
div.stButton > button {
    background-color: red;
    color: white;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-size:16px;
    font-weight:bold;
}
div.stButton > button:hover {
    background-color: yellow;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Filter data based on selected regions ------------------
filtered_df = df[df['Region'].isin(selected_regions)] if selected_regions else df

# ------------------ Home Page ------------------
if st.session_state.current_page == "Home":
    st.header("1 — Overview")
    if 'Happiness' in filtered_df.columns:
        st.metric("Average Happiness", f"{filtered_df['Happiness'].mean():.2f}")
    choice = st.radio("Select Countries to Display:", ["Top 10 Happiest", "Bottom 10 Least Happy"], horizontal=True)
    if choice == "Top 10 Happiest":
        sel_df = filtered_df[['Country','Happiness']].drop_duplicates(subset='Country').sort_values('Happiness', ascending=False).head(10)
        color_scale = 'Greens'
    else:
        sel_df = filtered_df[['Country','Happiness']].drop_duplicates(subset='Country').sort_values('Happiness', ascending=True).head(10)
        color_scale = 'Reds'
    if 'Happiness' in sel_df.columns:
        fig_bar = px.bar(sel_df, x='Happiness', y='Country', orientation='h', color='Happiness', color_continuous_scale=color_scale, text='Happiness')
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, title=f"{choice} Countries - Happiness")
        st.plotly_chart(fig_bar, use_container_width=True)

# ------------------ Insights Page ------------------
elif st.session_state.current_page == "Insights":
    st.header("2 — Key Drivers of Happiness")
    driver_cols = [c for c in numeric_cols if c in filtered_df.columns]
    if len(driver_cols) >= 2:
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(filtered_df[driver_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    
    st.subheader("Happiness vs Key Factors")
    factor_options = [col for col in driver_cols if col != 'Happiness']
    if 'Log_GDP' in factor_options:
        factor_options.remove('Log_GDP')
        factor_options = ['Log_GDP'] + factor_options
    if factor_options:
        selected_factor = st.selectbox("Select factor to compare with Happiness:", factor_options, index=0)
        if 'Happiness' in filtered_df.columns and selected_factor in filtered_df.columns:
            fig = px.scatter(filtered_df, x=selected_factor, y='Happiness', hover_name='Country', trendline='ols', title=f"Happiness vs {selected_factor}")
            st.plotly_chart(fig, use_container_width=True)

    st.header("3 — Regional Insights")
    if 'Happiness' in filtered_df.columns and 'Region' in filtered_df.columns:
        region_avg = filtered_df.groupby('Region', as_index=False)['Happiness'].mean().sort_values('Happiness', ascending=False)
        fig_region = px.bar(region_avg, x='Region', y='Happiness', color='Happiness', color_continuous_scale='Viridis', title="Average Happiness by Region")
        st.plotly_chart(fig_region, use_container_width=True)

# ------------------ Compare Page ------------------
elif st.session_state.current_page == "Compare":
    st.header("4 — Country Comparison")
    if len(compare_countries) < 2 or len(compare_countries) > 3:
        st.warning("Please select 2-3 countries for comparison")
    else:
        comp_df = filtered_df[filtered_df['Country'].isin(compare_countries)].drop_duplicates(subset='Country').set_index('Country')
        display_cols = [c for c in numeric_cols if c in comp_df.columns]
        st.subheader("Country Comparison Metrics")
        st.dataframe(comp_df[display_cols])
        
        st.subheader("Visual Comparison")
        long = comp_df[display_cols].reset_index().melt(id_vars='Country', var_name='Metric', value_name='Value')
        fig = px.bar(long, x='Metric', y='Value', color='Country', barmode='group')
        st.plotly_chart(fig, use_container_width=True)
        
        # Over/Under-performance vs Log GDP
        if 'Log_GDP' in df.columns and 'Happiness' in df.columns:
            df_dropna = df[['Log_GDP','Happiness']].dropna()
            if len(df_dropna) > 1:
                X = df_dropna[['Log_GDP']].values
                y = df_dropna['Happiness'].values
                reg = LinearRegression().fit(X, y)
                comp_with_log_gdp = comp_df[comp_df['Log_GDP'].notna()].copy()
                if not comp_with_log_gdp.empty:
                    comp_with_log_gdp['Expected_Happiness'] = reg.predict(comp_with_log_gdp[['Log_GDP']].values)
                    comp_with_log_gdp['Over_Under_Performance'] = comp_with_log_gdp['Happiness'] - comp_with_log_gdp['Expected_Happiness']
                    st.subheader("Over/Under-performance vs Log GDP-based Prediction")
                    fig_res = px.bar(
                        comp_with_log_gdp.reset_index(),
                        x='Country',
                        y='Over_Under_Performance',
                        color='Over_Under_Performance',
                        color_continuous_scale='RdBu',
                        text='Over_Under_Performance',
                        title="Happiness Residuals vs GDP Prediction"
                    )
                    st.plotly_chart(fig_res, use_container_width=True)
                else:
                    st.info("Selected countries don't have GDP data for performance comparison.")
            else:
                st.info("Insufficient data to create Log GDP-based prediction model.")
        else:
            st.info("GDP or Happiness column missing — cannot calculate over/under performance.")

# ------------------ Summary Page ------------------
elif st.session_state.current_page == "Summary":
    st.header("5 — Income Groups Analysis")
    if 'Log_GDP' in filtered_df.columns:
        lower_q = filtered_df['Log_GDP'].quantile(q_low)
        upper_q = filtered_df['Log_GDP'].quantile(q_high)
        def income_group(x):
            if pd.isna(x): return "Unknown"
            if x <= lower_q: return "Low"
            if x >= upper_q: return "High"
            return "Middle"
        filtered_df['Income_group'] = filtered_df['Log_GDP'].apply(income_group)
        ig_avg = filtered_df.groupby('Income_group', as_index=False)['Happiness'].mean()
        income_order = ['Low', 'Middle', 'High']
        ig_avg['Income_group'] = pd.Categorical(ig_avg['Income_group'], categories=income_order, ordered=True)
        ig_avg = ig_avg.sort_values('Income_group')
        st.subheader(f"Average Happiness by Income Group (Based on Log GDP)")
        fig = px.bar(ig_avg, x='Income_group', y='Happiness', color='Income_group',
                     color_discrete_map={'Low':'red','Middle':'orange','High':'green'})
        st.plotly_chart(fig, use_container_width=True)
        st.write("Counts per group:")
        st.write(filtered_df['Income_group'].value_counts())
    else:
        st.info("GDP column missing — cannot form income groups.")
    
    st.header("6 — Conclusions")
    correlations = {}
    for col in ['Log_GDP' if 'Log_GDP' in filtered_df.columns else 'GDP', 'Social_support', 'Life_expectancy', 'Freedom', 'Generosity', 'Corruption']:
        if col in filtered_df.columns and 'Happiness' in filtered_df.columns:
            corr = filtered_df['Happiness'].corr(filtered_df[col])
            correlations[col] = corr
    sorted_correlations = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)
    st.subheader("Main Findings")
    region_avg = filtered_df.groupby('Region')['Happiness'].mean() if 'Happiness' in filtered_df.columns else pd.Series()
    if not region_avg.empty:
        happiest_region = region_avg.idxmax()
        least_happy_region = region_avg.idxmin()
        conclusion_text = f"""
        Based on the analysis of the World Happiness data, the main findings are:
        - The strongest drivers of happiness are: 
          1. {sorted_correlations[0][0]} (r = {sorted_correlations[0][1]:.3f})
          2. {sorted_correlations[1][0]} (r = {sorted_correlations[1][1]:.3f})
          3. {sorted_correlations[2][0]} (r = {sorted_correlations[2][1]:.3f})
        - Income level (Log GDP) strongly correlates with happiness.
        - Regional differences: {happiest_region} is happiest, {least_happy_region} is least happy.
        """
    else:
        conclusion_text = "Regional happiness data not available."
    st.info(conclusion_text)
    st.subheader("All Correlation Values with Happiness")
    for factor, corr in sorted_correlations:
        st.write(f"{factor}: r = {corr:.3f}")

# ------------------ Download cleaned dataset ------------------
st.markdown("---")
buf = BytesIO()
df.to_csv(buf,index=False)
buf.seek(0)
st.download_button(
    label='⬇️ Download Full Cleaned Dataset (CSV)',
    data=buf,
    file_name='world_happiness_cleaned.csv',
    mime='text/csv',
    help="Download the cleaned and processed dataset including all columns and calculated income groups"
)
