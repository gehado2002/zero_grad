# 💳 Credit Card Fraud Detection – Machine Learning Project

## 📌 Project Overview
This project focuses on detecting **fraudulent digital payment transactions** using machine learning techniques.  
It applies a **complete end-to-end pipeline** including data profiling, preprocessing, feature engineering, handling class imbalance, and comparing multiple classification models.

📎 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1wyvQhnnJ48DLbpAYWx9mpj4CuNKBBuIu

---

## 📂 Dataset Description
**Digital Payment Fraud Dataset**

### 🛡️ Dataset Columns
| Column | Description |
|------|------------|
| distance_from_home | Distance between transaction location and cardholder’s home |
| distance_from_last_transaction | Distance from previous transaction |
| ratio_to_median_purchase_price | Transaction amount compared to user's median spending |
| repeat_retailer | Whether the retailer was used before (Boolean) |
| used_chip | Whether card chip was used (Boolean) |
| used_pin_number | Whether PIN was entered (Boolean) |
| online_order | Whether transaction was online (Boolean) |
| fraud | Target variable indicating fraud (Boolean) |

📊 Dataset Shape: **27,496 × 8**

---

## 🧾 Dataset Profiling
- Used **ydata_profiling** for automated exploratory analysis
- Identified:
  - No duplicate rows
  - Boolean features stored as numeric
  - Strong class imbalance in target variable

```bash
pip install ydata_profiling
