# 💳 Credit Card Fraud Detection

## 📌 Project Overview
This project focuses on detecting **fraudulent digital payment transactions** using machine learning techniques.  
The dataset represents real-world card transactions and is **highly imbalanced**, making fraud detection a challenging and realistic classification problem.

The notebook covers:
- Data profiling & preprocessing
- Handling class imbalance using **SMOTE**
- Feature engineering based on transaction behavior
- Multiple machine learning models
- Ensemble learning and performance comparison

📎 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1wyvQhnnJ48DLbpAYWx9mpj4CuNKBBuIu

---

## 🛡️ Digital Payment Fraud Dataset

### 📂 Dataset Shape
- **Rows:** 27,496  
- **Columns:** 8  
- **Target:** `fraud`

---

## 🧾 Column Description
| Column | Description |
|------|-------------|
| distance_from_home | Distance of the transaction from cardholder’s home |
| distance_from_last_transaction | Distance from the previous transaction |
| ratio_to_median_purchase_price | Transaction amount compared to user's median spending |
| repeat_retailer | Has the user purchased from this retailer before |
| used_chip | Whether the card chip was used |
| used_pin_number | Whether PIN was used |
| online_order | Indicates online transaction |
| fraud | **Target variable** (True = Fraud, False = Legitimate) |

---

## 🧾 Dataset Profiling
- Used **ydata-profiling** for automated EDA
- No missing values except 1 row in `online_order` and `fraud`
- All features numeric (boolean features converted to `bool`)

```bash
pip install ydata_profiling
