# 🦠 COVID-19 Global Analysis & Visualization 📊  

## 📌 Overview  
This project analyzes the **COVID-19 daily global dataset from WHO**, exploring trends in new cases, deaths, cumulative impact, and seasonal/region-wise distributions.  
The goal is to uncover **pandemic patterns**, visualize global effects, and demonstrate data preprocessing & visualization with **Plotly + Matplotlib**.  

---

## 📂 Dataset  
- **Source**: [WHO COVID-19 Global Data](https://covid19.who.int/data)  
- **Shape**: `491,040 rows × 8 columns`  
- **Key Variables**:  
  - 📅 `date_reported` – Daily date of record  
  - 🌍 `country`, `country_code`, `who_region`  
  - 🦠 `new_cases`, `cumulative_cases`  
  - ⚰️ `new_deaths`, `cumulative_deaths`  

---

## 🛠️ Preprocessing  
- ✅ Renamed all columns → lowercase, snake_case.  
- ✅ Missing values in `new_cases` & `new_deaths` handled with **fillna(0)**.  
- ✅ Converted `date_reported` → `datetime`.  
- ✅ Added new derived column: **season** (Winter, Spring, Summer, Autumn).  

---


## 🚀 Key Findings  
- **Winter** shows the highest spike in new cases & deaths globally.  
- Seasonal trends are **consistent across WHO regions** with varying magnitudes.  
- Data gaps were present (~57% missing in new cases, ~69% missing in new deaths) but imputed with zero.  
- Pandemic impact varied significantly by region, but all follow similar seasonal peaks.  

---

## 📦 Requirements  
```bash
pip install pandas numpy matplotlib plotly kaleido ydata-profiling
