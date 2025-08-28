# 🍽️ Zomato Restaurants – Exploratory Data Analysis 📊

## 📌 Overview
This project explores the **Zomato Restaurants dataset**, analyzing restaurant ratings, cuisines, customer preferences, and service trends across countries and cities.  
The goal is to uncover insights about food culture, market expansion opportunities, and dining patterns worldwide.

---

## 📂 Dataset
- **Source**: [Zomato Restaurants Dataset on Kaggle](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data)  
- **Shape**: `9551 rows × 21 columns`  
- **Key Variables**:
  - 🌍 Country, City, Locality  
  - 🍴 Cuisines  
  - 💰 Average Cost for Two, Currency, Price Range  
  - ⭐ Aggregate Rating, Rating Text, Votes  
  - 📱 Online Delivery, Table Booking  

---

## 🛠️ Preprocessing
- Renamed columns (lowercase, snake_case).  
- Dropped irrelevant fields (`restaurant_id`, `address`, etc.).  
- Removed null values in **cuisines**.  
- Mapped **country codes → country names**.  

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Market Insights
- **India dominates** the dataset (~90% of entries).  
- **New Delhi** has the highest restaurant count globally.  
- Choropleth maps highlight expansion opportunities in **USA, UAE, England, Brazil**.

### 🔹 Cuisine Analysis
- Top cuisines vary by country (e.g., **North Indian & Chinese in India**, **BBQ in USA**, **Pizza in Australia**).  
- Lollipop charts reveal cuisines with the **highest average ratings** (e.g., Italian in India, Sunda in Indonesia).  

### 🔹 Cost & Ratings
- Average cost for two varies significantly across countries.  
- High ratings (>4.5) often linked with **specialized cuisines** and premium price ranges.  

---

## 📈 Visualizations
- 📌 Choropleth maps for restaurant density by country  
- 📌 Styled HTML tables for top cuisines & cities  
- 📌 Stacked bar charts for cuisines distribution  
- 📌 Lollipop charts for best-rated cuisines  

*(Static PNG images are included for GitHub rendering.)*

---

## 🚀 Key Findings
- India is the **core market**, but global opportunities exist in USA, UAE, UK, and Brazil.  
- Customer preferences are **highly regional** – cuisines vary by country.  
- High cost ≠ high rating → value-for-money plays a big role.  
- Online delivery & table booking adoption differ across markets.  

---

## 📦 Requirements
```bash
pip install pandas numpy matplotlib seaborn plotly kaleido ydata-profiling
