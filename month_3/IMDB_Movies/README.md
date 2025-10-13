# 🎬 IMDB Movies Exploratory Data Analysis

## 📊 Data Source
**Primary Dataset**: [IMDB Movie Dataset on Kaggle](https://www.kaggle.com/datasets/yusufdelikkaya/imdb-movie-dataset)

---

## 🚀 Quick Access
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://imdb-movies-eda.streamlit.app/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wBmIx0Kk-Yw8Rhl36aJNSusCBeP5rGuF?usp=sharing)

---

## 📖 Overview
An interactive web application for exploring and analyzing the IMDB Top 1000 movies dataset. Discover trends, compare movies, and get personalized recommendations based on your preferences.


<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cnE0a2M5Y2h2ZjAxOXp3enJxZjRyZDF2Y24yYjMyeW81b3U5NWYxcSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/JUwN8RdJAnSPsvy5eZ/giphy.gif" width="800">

## 📊 Features

### 🏠 Dataset Preview
- **Data Overview**: Quick statistics and dataset information
- **Interactive Preview**: Browse the first 5 movies with posters
- **Filter Integration**: See how filters affect the dataset
- **Basic Metrics**: Total movies, columns, and time span

### 🔍 Basic Analysis
#### Univariate Analysis
- **Numerical Distributions**: Histograms for ratings, runtime, meta scores
- **Categorical Analysis**: Bar charts for genres, certificates, years
- **Statistical Insights**: Understand data distributions and patterns

#### Bivariate Analysis
- **Gross by Certificate**: Compare revenue across rating categories
- **Gross by Genre**: See which genres generate most revenue
- **Rating vs Gross**: Correlation between ratings and financial success
- **Votes vs Gross**: Relationship between popularity and revenue
- **Runtime vs Rating**: How movie length affects ratings
- **Meta Score vs Rating**: Compare critic and user ratings

### 💰 Top Movies Analysis
#### Top/Bottom Movies by Gross
- **Top 5 Highest Grossing**: Most financially successful movies
- **Bottom 5 Lowest Grossing**: Least financially successful movies
- **Detailed Comparisons**: Ratings, years, and key metrics

#### Sequels vs Standalone
- **Revenue Comparison**: Average gross of sequels vs original movies
- **Percentage Analysis**: Distribution between sequel types
- **Top Sequels**: Highest-grossing franchise movies

### 🎯 Movie Recommendations
- **Personalized Suggestions**: Get movies based on your preferences
- **Multiple Filters**: Genre, certificate, era, and actors
- **Smart Sorting**: Prioritized by rating and revenue
- **Detailed Profiles**: Complete movie information with posters

## 🛠️ Installation & Setup

### Option 1: 🎯 Live Demo (Recommended)
**👉 [Open Live Dashboard](https://imdb-movies-eda.streamlit.app/)**
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
# - main.py (Streamlit application)
# - imdb_top_1000.csv (Dataset)
# - requirements.txt (Dependencies)
# - README.md (Documentation)

# 2. Navigate to project directory
cd IMDB_Movies

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the application
streamlit run main.py
