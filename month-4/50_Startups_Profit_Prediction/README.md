💰 50 Startups Profit Prediction 📊
📌 Overview
Prediction of startup profits based on investments in R&D, Administration, Marketing, and State. End-to-end workflow: data loading, EDA, preprocessing, feature encoding & scaling, model training, and evaluation.

📂 Dataset
50_Startups.csv – financial data for 50 startups

🛡️ Columns
- R&D Spend → Money spent on Research & Development
- Administration → Money spent on Administration
- Marketing Spend → Money spent on Marketing
- State → State where the startup is located
- Profit → Target variable representing profit

📊 Dataset Shape
50 × 5

📎 Google Colab Notebook:
[50 Startups Profit Prediction](https://colab.research.google.com/drive/1cSptf6I--WtGcPZG9MlAgvSZ3cDyBBQY)

🛠️ Preprocessing
- Train-test split (85% train, 15% test)
- One-hot encoding for categorical column State
- Min-Max scaling for numerical features

📊 Exploratory Data Analysis (EDA)
- Histograms of numerical features (R&D Spend, Administration, Marketing Spend, Profit)
- Correlation of features with target variable Profit
- Average profit by State
- No missing values

📈 Model Training
- Linear Regression

📊 Model Evaluation
- R² on training set: 0.953
- 5-fold Cross-validation: [0.958, 0.962, 0.958, 0.958, 0.870]
- R² on test set: 0.905

✅ Key Takeaways
- R&D Spend is the strongest predictor of profit
- State has minor impact (encoded via OneHotEncoder)
- Linear Regression provides high accuracy on this dataset
