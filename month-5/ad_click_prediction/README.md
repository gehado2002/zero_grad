# 📢 Online Advertising Click Prediction

## 📌 Project Overview
This project aims to predict whether a user will **click on an online advertisement** based on their **demographics, browsing behavior, and engagement patterns**.  
It is formulated as a **binary classification problem** and includes end-to-end data analysis, feature engineering, and machine learning model comparison.

📎 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1p8sVpetp9ThbHKIhcndIFENpo-Eti-sS

---

## 📂 Dataset Description
**Advertising Dataset**  
**Shape:** 1000 rows × 10 columns  

### 🧾 Column Description
| Column Name | Description |
|------------|-------------|
| Daily Time Spent on Site | Average minutes spent on the website per day |
| Age | User age |
| Area Income | Average income of the user's area |
| Daily Internet Usage | Average daily internet usage (minutes) |
| Ad Topic Line | Advertisement headline |
| City | User city |
| Male | Gender (1 = Male, 0 = Female) |
| Country | User country |
| Timestamp | Date and time of ad interaction |
| Clicked on Ad | **Target variable** (1 = Clicked, 0 = Not Clicked) |

---

## 🎯 Project Objective
To build a **high-accuracy classification model** that predicts ad click behavior using:
- Demographic information  
- Online activity patterns  
- Time-based behavior  

---

## 🧾 Dataset Profiling
- Used **ydata-profiling** for automated EDA
- No missing values
- Balanced target distribution
- Mixed numerical and categorical features

```bash
pip install ydata_profiling
