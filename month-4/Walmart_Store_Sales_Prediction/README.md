🛒 Walmart Store Sales Prediction 🏬💰
📌 Overview
Predict weekly sales for Walmart stores using historical sales data. Includes EDA, feature engineering, scaling, temporal patterns, and multiple regression models for accurate forecasting.

📂 Dataset
Source: Walmart Dataset on Kaggle  
- 6435 rows × 8 columns
- Raw CSV: `Walmart.csv`

🛠️ Columns Explained
- Store 🏬 → Unique store ID
- Date 📅 → Week date of sales record
- Weekly_Sales 💵 → Target: total weekly sales
- Holiday_Flag 🎉 → 1 if the week includes a public holiday, else 0
- Temperature 🌡️ → Average weekly temperature
- Fuel_Price ⛽ → Average weekly fuel price
- CPI 📊 → Consumer Price Index in the area
- Unemployment 👷 → Weekly or monthly unemployment rate

🛠️ Preprocessing & Feature Engineering
- Converted `Date` to datetime and extracted temporal features
- Engineered lag features:
  - Sales_Lag_1 🕒 → Previous week’s sales
  - Rolling_Mean_3 🔄 → Average of last 3 weeks
- Handled missing values & dropped NaNs
- Target encoding for `Store` to reflect store-specific sales trends
- Scaled features using `StandardScaler`

📊 Exploratory Data Analysis (EDA)
- Univariate analysis: Sales mostly low, few high 🚀; Temperature & Fuel mostly normal 🌡️⛽
- Bivariate analysis: Holidays increase sales 🎉; store performance varies 🏬
- Multivariate analysis:
  - Weak correlations between weekly sales and most features
  - Store ID moderately impacts sales performance
- Correlation heatmaps to inspect relationships between features

📈 Regression Models Implemented
| Model                  | Train R² | Test R² | MAE      | RMSE     |
|------------------------|----------|---------|----------|----------|
| Linear Regression      | 0.989    | 0.985   | 43,822   | 70,864   |
| Ridge Regression       | 0.988    | 0.985   | 44,803   | 70,293   |
| Lasso Regression       | 0.988    | 0.985   | 45,152   | 70,341   |
| ElasticNet Regression  | 0.987    | 0.984   | 45,598   | 71,643   |
| Support Vector Regression (SVR) | 0.948 | 0.952 | ~63k | ~114k |
| KNeighbors Regressor   | 1.000    | 0.960   | ~64k     | ~125k    |

✅ Key Insights
- Linear models with polynomial features outperform SVR and KNN in terms of R², MAE, and RMSE
- Holidays have significant positive impact on sales 🎉
- Store-specific trends captured using target encoding improve prediction
- Rolling and lag features help the model capture temporal sales patterns

💾 Model Saving
- Linear Regression: `linear_regression_model.pkl`
- Best SVR: `best_svr_model.pkl`
- KNN Regressor: `best_knn_model.pkl`

📎 Google Colab Notebook:
[Walmart Store Sales Prediction](https://colab.research.google.com/drive/1WEol6x-O6rJWcVXZ_R3t8VPeuXr3s3OU?usp=sharing)
