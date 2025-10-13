# ✈️ Airline Passenger Satisfaction Dashboard

## 📊 Data Source
**Primary Dataset**: [Airline Passenger Satisfaction Dataset on Kaggle](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

---

## 🚀 Quick Access
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-airline-satisfaction-app.streamlit.app/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Istu0SkGD9TC4iiblg_Xeb5IZvUKig8k?usp=sharing)

---

## 📖 Overview
An interactive web application for analyzing airline passenger satisfaction data. Explore customer experience metrics, identify key satisfaction drivers, and compare airline service performance across different categories.

![Airline Dashboard](https://www.elliott.org/wp-content/uploads/No-Room.png)

## 📊 Features

### 🏠 Home - Overview
- **Overall Satisfaction Metrics**: Key performance indicators and satisfaction scores
- **Demographic Analysis**: Passenger distribution by gender, customer type, travel class
- **Flight Information**: Travel type, class distribution, and flight distance analysis
- **Real-time Analytics**: Dynamic metrics based on filtered data

### 🔍 Insights - Key Drivers
- **Feature Importance**: Identify which factors most impact passenger satisfaction
- **Correlation Analysis**: Heatmaps showing relationships between service categories
- **Service Category Analysis**: Deep dive into specific service aspects
- **Statistical Trends**: Regression analysis and trend identification

### 📊 Compare - Service Analysis
- **Multi-dimensional Comparison**: Compare different passenger segments
- **Satisfaction Gap Analysis**: Identify areas for improvement
- **Performance Metrics**: Side-by-side service category comparisons
- **Detailed Breakdown**: Numerical analysis of all satisfaction factors

### 📈 Predictive Analytics
- **Satisfaction Prediction**: Machine learning models to predict passenger satisfaction
- **Feature Impact**: Understand how different factors influence satisfaction scores
- **Model Performance**: Accuracy metrics and validation results
- **What-if Analysis**: Simulate how changes in services affect satisfaction

## 🛠️ Installation & Setup

### Option 1: 🎯 Live Demo (Recommended)
**👉 [Open Live Dashboard](https://your-airline-satisfaction-app.streamlit.app/)**
- No installation required
- Real-time analysis
- Full interactive functionality

### Option 2: 🐍 Python Local Installation

#### Prerequisites
- Python 3.7 or higher
- pip package manager

#### Step-by-Step Installation
```bash
# 1. Download the project files
# Ensure you have:
# - airline_streamlit_code.py
# - airline_passenger_satisfaction.csv  
# - requirements.txt
# - README.md

# 2. Navigate to project directory
cd airline-passenger-satisfaction

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the application
streamlit run airline_streamlit_code.py
