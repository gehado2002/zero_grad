🩺 Breast Cancer Classification – Predict Malignant vs Benign Tumors 💗

📌 Overview
This project classifies breast tumors as malignant or benign using the famous Breast Cancer Wisconsin dataset. Includes EDA, feature selection, scaling, model training, and evaluation.

📂 Dataset
- Source: `/content/data(1).csv`
- 569 entries × 31 columns
- Features: Tumor measurements (radius, texture, perimeter, area, smoothness, compactness, concavity, symmetry, fractal dimension) – mean, SE, and worst values
- Target: `diagnosis` (B = benign, M = malignant)

🛠️ Data Preprocessing
- Dropped `id` and `Unnamed: 32` columns
- Converted diagnosis to numeric (0 = Benign, 1 = Malignant)
- Train-test split: 80% train, 20% test (stratified)

📊 Exploratory Data Analysis (EDA)
- 💗 Class distribution: Balanced with slight predominance of benign tumors
- 🔹 Numerical feature distributions visualized for all tumor measurements
- 📈 Feature correlation heatmap revealed multicollinearity between some features

⚙️ Feature Engineering & Selection
- Removed highly correlated features (correlation > 0.9) to reduce redundancy
- Scaled features using `StandardScaler`

  
🧠 Model Training
- Logistic Regression with GridSearchCV to find best hyperparameters
- Best Parameters: `C=1000, penalty='l2'`
- Train Accuracy: 0.982
- Test Accuracy: 0.965

📊 Model Evaluation
- Confusion Matrix:

- Precision / Recall / F1-Score: ~0.95–0.97 for both classes
- ROC AUC Score: 0.993 (excellent discriminative power)

🔹 Visualizations
- Class distribution with soft pink-purple color scheme
- Feature histograms & distributions
- Feature correlation heatmap (PuRd palette)
- Confusion matrix heatmap
- ROC curve with shaded area and AUC display

📈 Key Insights
- Logistic Regression performs very well for this dataset (accuracy ~96.5%)
- Top features influencing classification include radius, texture, concavity, and compactness metrics
- Feature selection improved model interpretability and reduced redundancy
- Soft color palettes used throughout for clarity and presentation quality

📎 Google Colab Notebook:
[Breast Cancer Classification](https://colab.research.google.com/drive/1-BLgI4Hyi1f34w8wUbGI3oUbV7Th_FPK?usp=sharing)
- Applied `SelectKBest` (ANOVA F-test) to select top 10 most predictive features:
