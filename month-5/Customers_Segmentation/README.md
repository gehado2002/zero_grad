# 👥 Customer Segmentation Using RFM Analysis & Clustering

## 📌 Project Overview
This project focuses on **customer segmentation** using a marketing campaign dataset.  
By analyzing **customer demographics, purchase behavior, and engagement**, we apply **RFM Analysis** combined with **K-Means and Hierarchical Clustering** to identify meaningful customer groups.

The segmentation results can help businesses:
- Target customers more effectively
- Improve marketing campaign success
- Understand high-value and low-engagement customers

📎 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1XPQbO6yZZIYdNLJiND6SyUGz8b93pAD6

---

## 📂 Dataset Description
**Marketing Campaign Dataset**  
Each row represents a single customer with demographic, behavioral, and campaign-related attributes.

---

## 👤 Customer Information
| Column | Description |
|------|-------------|
| ID | Unique customer identifier |
| Year_Birth | Year of birth |
| Education | Education level |
| Marital_Status | Marital status |
| Income | Annual household income |

---

## 👨‍👩‍👧‍👦 Household Information
| Column | Description |
|------|-------------|
| Kidhome | Number of children |
| Teenhome | Number of teenagers |

---

## 📅 Customer Timeline
| Column | Description |
|------|-------------|
| Dt_Customer | Date customer joined |
| Recency | Days since last purchase |

---

## 🛍️ Product Spending (Last 2 Years)
| Column | Description |
|------|-------------|
| MntWines | Wine spending |
| MntFruits | Fruits spending |
| MntMeatProducts | Meat spending |
| MntFishProducts | Fish spending |
| MntSweetProducts | Sweets spending |
| MntGoldProds | Gold spending |

---

## 🧾 Purchase Behavior
| Column | Description |
|------|-------------|
| NumDealsPurchases | Purchases with discounts |
| NumWebPurchases | Web purchases |
| NumCatalogPurchases | Catalog purchases |
| NumStorePurchases | In-store purchases |
| NumWebVisitsMonth | Monthly website visits |

---

## 📢 Marketing Campaigns
| Column | Description |
|------|-------------|
| AcceptedCmp1–5 | Accepted previous campaigns (1 = Yes, 0 = No) |
| Complain | Customer complained (1 = Yes, 0 = No) |

---

## ⚙️ Constant Columns
| Column | Description |
|------|-------------|
| Z_CostContact | Fixed contact cost |
| Z_Revenue | Fixed revenue |

---

## 🎯 Target Variable (Removed for Clustering)
| Column | Description |
|------|-------------|
| Response | Accepted last campaign (1 = Yes, 0 = No) |

---

## 🧾 Dataset Profiling
- Used **ydata-profiling** for automated EDA
- Checked missing values, distributions, correlations

```bash
pip install ydata_profiling
