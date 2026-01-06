# 🛒 Online Retail Customer Segmentation (RFM & Clustering)

## 📌 Project Overview
This project analyzes an **Online Retail dataset** to understand customer purchasing behavior and perform **customer segmentation** using **RFM Analysis** and **Clustering techniques**.  
The goal is to identify distinct customer groups to support **marketing strategy, personalization, and business decision-making**.

📎 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1xdwUc5TjoFhJxcwJ1pDPZsRS8r_1F_os

---

## 📂 Dataset Description
**Online Retail Dataset**  
Transactional data for a UK-based online store.

### 🧾 Dataset Columns
| Column | Description |
|------|-------------|
| InvoiceNo | Unique transaction ID (starting with `C` indicates cancellation/return) |
| StockCode | Product identifier |
| Description | Product description |
| Quantity | Number of items purchased (negative → returns) |
| InvoiceDate | Date & time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Customer country |

---

## 🎯 Project Objectives
- Clean and preprocess real-world retail data
- Analyze purchasing behavior
- Perform **RFM Analysis**
- Segment customers using **K-Means** and **Hierarchical Clustering**
- Visualize and compare clustering results

---

## 🧾 Dataset Profiling
- Used **ydata-profiling** for automated EDA
- Used **missingno** for missing-value visualization
- Identified missing values, duplicates, and data quality issues

```bash
pip install ydata_profiling missingno
