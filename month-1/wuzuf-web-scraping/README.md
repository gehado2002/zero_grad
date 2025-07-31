# 🛠️ Wuzzuf Job Scraper – Python Web Scraping Project  

A Python-based web scraper that extracts **job postings from Wuzzuf** for multiple job categories and saves them as CSV files.  
It uses **Requests + BeautifulSoup + Pandas** to collect job details like title, company, occupation, and job description.  

---

## 📌 Features  
✅ Scrapes job postings for **Data Analysis, Data Science, and Business Intelligence**  
✅ Extracts job **title, company, link, occupation, and job specs**  
✅ Saves results into **CSV files for each job category**  
✅ Easy to customize for any job title or number of pages  

---

## 🎯 How It Works  
1️⃣ The program visits Wuzzuf job search pages.  
2️⃣ Extracts job details (title, company, occupation, specs, and link).  
3️⃣ Saves data into CSV files:  
   - `data analysis_jobs_in_egypt.csv`  
   - `data science_jobs_in_egypt.csv`  
   - `business intelligence_jobs_in_egypt.csv`  

---

## 📸 Example Output (Console)
```
Scraping data for 'data analysis'...
Scraping data for 'data science'...
Scraping data for 'business intelligence'...
🛤️data analysis jobs scraped successfully
🛤️data science jobs scraped successfully
🛤️business intelligence jobs scraped successfully
😀Done
```
