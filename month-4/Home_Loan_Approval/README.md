🏠 Home Loan Approval Prediction 💰
📌 Overview
Predict whether a home loan will be approved based on applicant and financial information. Includes EDA, preprocessing, feature engineering, scaling, handling class imbalance, model training, and evaluation.

📂 Dataset
Source: Kaggle – Home Loan Approval Dataset
Files:
- loan_sanction_train(1).csv → training data
- loan_sanction_test(1).csv → test data

🛡️ Columns
- Loan_ID 🆔 → Unique ID
- Gender 👤 → Male / Female
- Married 💍 → Yes / No
- Dependents 👶 → 0,1,2,3+
- Education 🎓 → Graduate / Not Graduate
- Self_Employed 💼 → Yes / No
- ApplicantIncome 💰 → Monthly income
- CoapplicantIncome 👥💰 → Monthly income of co-applicant
- LoanAmount 💵 → Loan requested (in thousands)
- Loan_Amount_Term 📅 → Term in months
- Credit_History 🏦 → 1.0 good, 0.0 bad
- Property_Area 🏠 → Urban, Semiurban, Rural
- Loan_Status ✅❌ → Y / N (target)

🛠️ Preprocessing & Feature Engineering
- Dropped Loan_ID
- Handled missing values (KNNImputer for numeric, mode/fill for categorical)
- Log transform and Winsorization for outliers
- Engineered features:
  - TotalIncome = ApplicantIncome + CoapplicantIncome
  - Debt_Income_Ratio = LoanAmount / TotalIncome
  - Family_Size = Dependents + 1
- One-hot encoding for Property_Area
- Label encoding for Gender, Married, Education, Self_Employed, Loan_Status
- Scaled numeric columns with StandardScaler
- Balanced classes with SMOTE

📊 EDA Highlights
- Histograms for incomes, LoanAmount, Loan_Amount_Term
- Correlation analysis
- Outlier treatment with log transform & Winsorization
- Categorical distributions & missing value analysis

📈 Models & Performance
- Logistic Regression → Accuracy 0.8618 ✅ Best Model
- K-Nearest Neighbors → Accuracy 0.7967
- Support Vector Classifier → Accuracy 0.8130

💾 Models Saved
- improved_logistic_model.pkl
- improved_knn_model.pkl
- improved_svc_model.pkl

📎 Google Colab Notebook:
[Home Loan Approval Prediction](https://colab.research.google.com/drive/1bCpi8VKqZYyLz1LIUEG32uqYBnbEnI8C?usp=sharing)
