🚢 Titanic Survival Prediction – Logistic Regression Analysis ❤️🖤

📌 Overview
This project predicts passenger survival on the Titanic using logistic regression. It includes EDA, feature engineering, missing value imputation, encoding, scaling, and model evaluation with custom thresholds.

📂 Dataset
- Training set: 891 rows × 12 columns
- Test set: 418 rows × 11 columns
- Features: Passenger info (Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Name, Ticket, Cabin)
- Target: `Survived` (0 = No, 1 = Yes)

🛠️ Data Preprocessing
- Dropped `Cabin` (too many missing) and `PassengerId` (non-informative)
- Imputed missing `Age` using median age per `Pclass`, `Sex`, and `Title` extracted from Name
- Imputed missing `Embarked` values
- Feature engineering:
  - `FamilySize` = SibSp + Parch + 1
  - `IsAlone` = 1 if alone, 0 otherwise
  - `FarePerPerson` = Fare / FamilySize
  - `AgeGroup` = categorical age bins (Child, Teen, Adult, Senior, Elder)

📊 Exploratory Data Analysis (EDA)
- Class distribution: ~38% survived, ~62% did not
- Histograms for numeric features with Titanic-themed style (black + red)
- Feature correlation heatmap visualized in Titanic color scheme

⚙️ Data Encoding
- One-hot encoding for categorical features: AgeGroup, Sex, Embarked, Title
- Ensured test set columns match training set

⚖️ Feature Scaling
- StandardScaler applied on numeric features: Pclass, Age, SibSp, Parch, Fare, FamilySize, FarePerPerson

- 5-fold cross-validation accuracy: 0.830 ± 0.033
- Train accuracy: 0.837
- Validation accuracy: 0.846

🎯 Model Evaluation
- ROC curve: AUC ≈ 0.90
- Youden's J method used to select optimal threshold: 0.35
- Confusion Matrix (using threshold ~0.29):
- Precision / Recall / F1-Score:
  - Class 0 (Not Survived): precision 0.90, recall 0.75, f1 0.82
  - Class 1 (Survived): precision 0.71, recall 0.88, f1 0.78
- Accuracy: 0.80

🔹 Visualizations
- Titanic-style EDA plots (black/red)
- Feature correlation heatmap with Titanic colors
- Confusion matrix with improved readability
- ROC curve with AUC

📈 Key Insights
- Logistic Regression performs well with feature engineering and scaling (~84–85% validation accuracy)
- Custom threshold tuning improves recall for survivors
- Important predictive features include Pclass, Sex, Age, Fare, and family-related metrics

📎 Google Colab Notebook:
[Titanic Survival Prediction](https://colab.research.google.com/drive/1Kmf58iLRsLPf0SuWeTbxyh1UFxL7TPee?usp=sharing)


🧠 Model Training
- Logistic Regression with `GridSearchCV` to optimize hyperparameters:
