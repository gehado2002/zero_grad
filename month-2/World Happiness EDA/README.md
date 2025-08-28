# 🌍 World Happiness Report 2021 – EDA Project 📊

## 📌 Overview
This project analyzes the **World Happiness Report 2021** dataset to explore factors influencing happiness across countries.  
The analysis covers data cleaning, feature engineering, visualizations, and regional/country comparisons.

---

## 📂 Dataset
- **Source**: [Kaggle – World Happiness Report 2021](https://www.kaggle.com)  
- **Shape**: `149 rows × 20 columns` (reduced after preprocessing)  
- **Target Variable**: `Happiness (Ladder Score)`  

### Main Features:
- 💰 **GDP per capita**  
- 🤝 **Social Support**  
- 🩺 **Life Expectancy**  
- 🕊️ **Freedom**  
- 🎁 **Generosity**  
- ⚖️ **Corruption Perception**  
- 🌍 **Country & Region**

---

## 🛠️ Data Preprocessing
- Dropped redundant columns (`whiskers, residuals, explained by …`).  
- Renamed columns for readability (`Country`, `Region`, `GDP`, `Life_Expectancy`, etc.).  
- Created new feature: `Happiness_Level` (Low vs High).  
- No missing or duplicate values.  

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Correlations
- Strong **positive correlation**: GDP 💰, Social Support 🤝, Life Expectancy 🩺, Freedom 🕊️  
- Weak correlation: Generosity 🎁  
- Strong **negative correlation**: Corruption ⚖️  

### 🔹 Visual Insights
- **Regression plots** → Show direct relationship between factors and happiness.  
- **Histograms (red shades)** → Contrast high vs low happiness distributions.  
- **Correlation heatmap** → GDP, health, and freedom dominate happiness scores.  
- **Boxplots by region** → Western Europe, North America, Oceania rank highest.  
- **Regional comparison**:
  - Highest Region → Happiness driven by **Social Support**  
  - Lowest Region → Happiness limited by **Corruption**  
- **Country comparison**:
  - **Finland vs Afghanistan** → Finland leads in Social Support, Freedom, Life Expectancy, GDP.  
  - Afghanistan scores higher only in **Corruption perception** (worse).  

---

## 📈 Key Findings
- Income and health are the **strongest drivers** of happiness.  
- Social trust (low corruption, strong support) significantly increases well-being.  
- Regions differ: Western Europe scores highest, Sub-Saharan Africa lowest.  
- Happiness gaps between countries reflect **economic + social + governance factors**.  

---

## 🚀 Next Steps
- Apply clustering to group countries by happiness drivers.  
- Use regression / ML to predict happiness scores.  
- Compare with 2022/2023 reports for trend analysis.  

---

## 📦 Requirements
```bash
pip install pandas numpy matplotlib seaborn plotly ydata-profiling
