🏡 House Pricing Data Analysis & Prediction 🏠💰
📌 Overview
Predict median house prices using California housing data. Includes EDA, preprocessing, feature engineering, scaling, outlier handling, and Random Forest regression modeling.

📂 Dataset
Source: Hands-On ML 2nd Edition – California Housing Dataset
- 20640 rows × 10 columns
- Raw CSV: [housing.csv](https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv)

🛡️ Columns
- longitude 📍 → Geographic coordinate
- latitude 📍 → Geographic coordinate
- housing_median_age 🏠 → Median age of houses
- total_rooms 🛏️ → Total rooms in district
- total_bedrooms 🛏️→ Total bedrooms in district
- population 👥 → Population of district
- households 🏘️ → Number of households
- median_income 💰 → Median income in block
- median_house_value 💵 → Median house value (target)
- ocean_proximity 🌊 → Location relative to ocean (categorical)

🛠️ Preprocessing & Feature Engineering
- Split into train (80%) and test (20%) sets
- Handled missing values in total_bedrooms
- Engineered features:
  - income_per_room = median_income / total_rooms
  - bedrooms_per_household = total_bedrooms / households
  - rooms_per_person = total_rooms / population
- Removed outliers above 99th percentile for key features
- Scaled numeric columns using RobustScaler
- One-hot encoded categorical feature: ocean_proximity

📊 EDA Highlights
- Histograms for numeric features
- Boxplots for outlier detection
- Correlation analysis with target variable median_house_value
- Geographical scatter map of house prices showing coastal impact

📈 Modeling
- Random Forest Regressor:
  - n_estimators=100, random_state=42, n_jobs=-1
  - R² on test set: 0.827
- Cross-validated RMSE to check model stability
- Full pipeline with preprocessing and encoding for consistent data transformation

🔍 Key Insights
- Median house value strongly correlates with median_income and location
- Coastal areas 🌊 tend to have higher house values
- Feature engineering improved model predictions

📎 Google Colab Notebook:
[Tuning House Pricing Data](https://colab.research.google.com/drive/100gqfMfj1xWVyiIhuIaZzEAgFt45dPBf?usp=sharing)
