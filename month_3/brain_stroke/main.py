import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Brain Stroke Analysis - Health Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fun, colorful CSS styling with medical theme
st.markdown("""
<style>
    /* Main app background - Light and cheerful */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #333333;
    }
    
    /* Fun header with gradient */
    .main-header {
        font-size: 3rem;
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 50%, #45B7D1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
        font-family: 'Arial', sans-serif;
        padding: 20px 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Colorful sub headers */
    .sub-header {
        font-size: 1.8rem;
        color: #FF6B6B;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 245, 245, 0.9) 100%);
        padding: 15px 20px;
        border-radius: 15px;
        margin: 2rem 0 1rem 0;
        font-weight: 600;
        border-left: 5px solid #FF6B6B;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Playful metric cards */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 25px 20px;
        border-radius: 20px;
        border: 2px solid #4ECDC4;
        margin: 15px 0;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        color: #333;
    }
    
    .metric-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 35px rgba(78, 205, 196, 0.3);
        border-color: #FF6B6B;
    }
    
    /* Fun emergency alert */
    .emergency-alert {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 50%, #FF6B6B 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        border: 3px solid #FFE66D;
        margin: 20px 0;
        text-align: center;
        font-weight: 700;
        font-size: 1.2rem;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    /* Simple GIF container without borders */
    .gif-container {
        text-align: center;
        margin: 30px 0;
        padding: 0;
    }
    
    /* Colorful sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Sidebar text color - FIXED: Changed to bright yellow for visibility */
    section[data-testid="stSidebar"] * {
        color: #FFE66D !important;
    }
    
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5,
    section[data-testid="stSidebar"] h6,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div,
    section[data-testid="stSidebar"] label {
        color: #FFE66D !important;
    }
    
    /* Sidebar radio buttons - ensure text is visible */
    .stRadio [data-testid="stMarkdownContainer"] p {
        color: #FFE66D !important;
        font-weight: 600;
    }
    
    /* Sidebar buttons */
    section[data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%) !important;
        color: #2c3e50 !important;
        border: 2px solid #FFE66D !important;
        font-weight: 600;
    }
    
    /* Fun button styling */
    .stButton>button {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4) !important;
        font-size: 1rem !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 8px 25px rgba(78, 205, 196, 0.6) !important;
    }
    
    /* Colorful radio buttons and select boxes */
    .stRadio > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #4ECDC4;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        border: 2px solid #4ECDC4 !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Colorful slider */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%) !important;
    }
    
    /* Fun dataframe styling */
    .stDataFrame {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        border-radius: 15px !important;
        border: 2px solid #FFE66D !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    /* Colorful tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        gap: 5px;
        border-radius: 15px;
        padding: 5px;
        border: 2px solid #4ECDC4;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        color: #333 !important;
        border-radius: 12px !important;
        border: 2px solid transparent !important;
        padding: 10px 20px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4) !important;
        transform: scale(1.05);
    }
    
    /* Metric value styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
        border: 2px solid #FFE66D !important;
        border-radius: 20px !important;
        padding: 20px !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    /* Success, warning, error messages with colors */
    .stSuccess {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%) !important;
        border: 2px solid #28a745 !important;
        border-radius: 15px !important;
        color: #155724 !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%) !important;
        border: 2px solid #ffc107 !important;
        border-radius: 15px !important;
        color: #856404 !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%) !important;
        border: 2px solid #dc3545 !important;
        border-radius: 15px !important;
        color: #721c24 !important;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        border-radius: 10px;
    }
    
    /* Fun hover effects for all interactive elements */
    .element-container:hover {
        transform: translateY(-2px);
        transition: transform 0.3s ease;
    }
    
    /* Health tips in sidebar */
    .health-tips-sidebar {
        background: rgba(255, 255, 255, 0.2) !important;
        padding: 15px;
        border-radius: 15px;
        margin-top: 20px;
    }
    
    .health-tips-sidebar h5,
    .health-tips-sidebar p {
        color: #FFE66D !important;
        text-align: center;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(r'healthcare-dataset-stroke-data.csv')
        
        # Data cleaning
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)
        
        # Add derived columns
        bins_age = [0, 12, 18, 35, 50, 100]
        labels_age = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
        df['age_group'] = pd.cut(df['age'], bins=bins_age, labels=labels_age)
        
        bins_bmi = [0, 18.5, 24.9, 29.9, 100]
        labels_bmi = ['Underweight', 'Normal', 'Overweight', 'Obese']
        df['bmi_category'] = pd.cut(df['bmi'], bins=bins_bmi, labels=labels_bmi)
        
        return df
        
    except FileNotFoundError:
        st.error("❌ File 'healthcare-dataset-stroke-data.csv' not found.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading dataset: {str(e)}")
        return None

# Load data
df = load_data()

# Main header with fun gradient
st.markdown('<h1 class="main-header">🧠 BRAIN STROKE ANALYSIS - HEALTH DASHBOARD</h1>', unsafe_allow_html=True)

# New GIF without any borders or container
st.markdown("""
<div class="gif-container">
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3BjNHFmYnczOTdlNWs5Nnhkaml0eTN0OTR3Z3FmY3R1NHptdzJzaSZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/ZGIO2lAIEFq0E9T99X/giphy.gif" 
         width="500">
</div>
""", unsafe_allow_html=True)

# Fun emergency warning with bounce animation
st.markdown("""
<div class="emergency-alert">
    ⚠️ 🚨 HEALTH ALERT - KNOW THE SIGNS! 🚨 ⚠️<br>
    <strong>F.A.S.T. = Face • Arms • Speech • Time</strong><br>
    <span style="font-size: 1rem;">Don't wait - act fast!</span>
</div>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 Home"

# Colorful sidebar navigation
st.sidebar.markdown("""
<div style="text-align: center; margin-bottom: 30px; padding: 20px; background: rgba(255,255,255,0.2); border-radius: 15px;">
    <h2 style="color: #FFE66D; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎯 HEALTH NAVIGATOR</h2>
</div>
""", unsafe_allow_html=True)

page_options = ["🏠 Home", "📊 Data Overview", "📈 Analysis", "🎯 Findings", "🤖 Prediction"]
selected_page = st.sidebar.radio("", page_options, index=page_options.index(st.session_state.current_page))

# Update session state
st.session_state.current_page = selected_page

# Fun quick assessment button
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="text-align: center; padding: 15px; background: rgba(255,255,255,0.2); border-radius: 15px;">
    <h4 style="color: #FFE66D; margin-bottom: 15px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">⚡ QUICK HEALTH CHECK</h4>
</div>
""", unsafe_allow_html=True)

if st.sidebar.button("🎯 Check My Health Risk", use_container_width=True):
    st.session_state.current_page = "🤖 Prediction"

# Add some fun emojis and tips in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div class="health-tips-sidebar">
    <h5>💡 HEALTH TIPS</h5>
    <p style="font-size: 0.9rem;">
    🏃 Stay Active • 🥗 Eat Healthy • 😴 Sleep Well • 💧 Stay Hydrated
    </p>
</div>
""", unsafe_allow_html=True)

# Import page modules
try:
    from home_page import show_home_page
    from data_overview import show_data_overview_page
    from analysis import show_analysis_page
    from findings import show_findings_page
    from prediction import show_prediction_page
except ImportError:
    st.error("⚠️ Some page modules are missing. Please ensure all Python files are in the same directory.")

# Display the selected page
if st.session_state.current_page == "🏠 Home":
    show_home_page()

elif st.session_state.current_page == "📊 Data Overview":
    show_data_overview_page(df)

elif st.session_state.current_page == "📈 Analysis":
    show_analysis_page(df)

elif st.session_state.current_page == "🎯 Findings":
    show_findings_page(df)

elif st.session_state.current_page == "🤖 Prediction":
    show_prediction_page()