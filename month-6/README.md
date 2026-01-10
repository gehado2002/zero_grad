🚴‍♂️ **Bike Sharing Demand Prediction**

📌 **Project Overview**  
This project predicts the total number of bike rentals using historical bike sharing data.  
The focus is on building a **Deep Learning model** and performing **data preprocessing, feature engineering, and outlier handling**.

---

📎 **Google Colab Notebook:**  
[Open in Colab](https://colab.research.google.com/drive/1H2FhX8LcP4lYrCWWjjSlPkfpX2Tb2Q4l?usp=sharing)

---

🛠️ **Technologies Used**  
- Python 3  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Scikit-learn  
- TensorFlow / Keras  

---

📂 **Dataset**  
**Bike Sharing Hourly Dataset**  
- Rows: 17,379  
- Columns: 17  
- Target: `cnt` (total bike rentals)

**Column Description**  

| Column | Description |
|--------|------------|
| instant | Record index |
| dteday | Date |
| season | Season (1:winter, 2:spring, 3:summer, 4:fall) |
| yr | Year (0:2011, 1:2012) |
| mnth | Month (1 to 12) |
| hr | Hour of the day (0 to 23) |
| holiday | Whether the day is a holiday |
| weekday | Day of the week (0 to 6) |
| workingday | 1 if working day, 0 otherwise |
| weathersit | Weather situation (1 to 4) |
| temp | Temperature in Celsius |
| atemp | "Feels like" temperature (dropped in this project) |
| hum | Humidity |
| windspeed | Wind speed |
| casual | Number of casual users (dropped) |
| registered | Number of registered users (dropped) |
| cnt | Total rental count (Target) |

---

🧾 **EDA & Profiling**  
- Automated profiling using `ydata-profiling`  
- Checked for missing values (none significant)  
- Numeric & categorical features identified  
- Visualizations for trends by hour, season, and weather  

```bash
pip install ydata_profiling

