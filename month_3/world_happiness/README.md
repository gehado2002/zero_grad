# 🌍 World Happiness Dashboard

## 📊 Data Source
**Primary Dataset**: [World Happiness Report on Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness)  

---

## 🚀 Quick Access
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://world-happiness-mini-app.streamlit.app/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1d255zrcW8xCDlBhgW4_BtP7ELHDqvBP4?usp=sharing)

---

## 📖 Overview
An interactive web application for analyzing and visualizing global happiness data from the World Happiness Report. Explore happiness trends, compare countries, and discover the key factors that contribute to national well-being.

![Dashboard Preview](https://ds8526jcpbygs.cloudfront.net/wp-content/uploads/2016/08/happysad.jpg)

## 📊 Features

### 🏠 Home - Overview
- **Top/Bottom Rankings**: View the 10 happiest and least happy countries
- **Interactive Visualizations**: Bar charts with color-coded happiness scores
- **Real-time Metrics**: Average happiness score for selected regions

### 🔍 Insights - Key Drivers
- **Correlation Analysis**: Heatmap showing relationships between happiness factors
- **Scatter Plots**: Explore happiness vs GDP, social support, life expectancy, etc.
- **Regional Analysis**: Compare average happiness across different world regions
- **OLS Trendlines**: Statistical trends with linear regression

### 📊 Compare - Country Comparison
- **Multi-country Analysis**: Compare 2-3 countries across all happiness metrics
- **Performance Analysis**: Over/under-performance vs GDP-based expectations
- **Grouped Visualizations**: Side-by-side comparison bars
- **Detailed Metrics Table**: Numerical comparison of all factors

### 📈 Summary - Advanced Analytics
- **Income Group Analysis**: Low/Middle/High income categorization based on GDP
- **Statistical Correlations**: Ranked list of happiness drivers by correlation strength
- **Key Findings**: Automated insights generation
- **Data Export**: Download cleaned and processed datasets

## 🛠️ Installation & Setup

### Option 1: 🎯 Live Demo (Recommended)
**👉 [Open Live Dashboard](https://world-happiness-mini-app.streamlit.app/)**
- No installation required
- Always up-to-date
- Full functionality

### Option 2: 🐍 Python Local Installation

#### Prerequisites
- Python 3.7 or higher
- pip package manager

#### Step-by-Step Installation
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/world-happiness-dashboard.git

# 2. Navigate to project directory
cd world-happiness

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the application
streamlit run world_happinessstreamlit_code.py
