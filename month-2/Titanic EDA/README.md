# 🚢 Titanic Data Analysis 📊

## 📌 Overview
Exploratory analysis of the Titanic dataset to uncover survival patterns based on demographics, ticket info, and cabins.  

---

## 🛠️ Preprocessing
- Dropped `PassengerId`  
- Filled missing values (`Embarked`, `Cabin`)  
- Created new features:  
  - **Title** (from Name)  
  - **Shared_Ticket** (shared vs individual)  
  - **Ticket_Prefix**  
  - **Cabin_Deck**  
  - **Family_Size** = `SibSp + Parch + 1`  

---

## 📊 Key Insights
- **Gender**: Females survived more (~74%) vs males (~19%).  
- **Class**: 1st class survival ~63%, 3rd class ~24%.  
- **Age**: Children (<10 yrs) had higher survival.  
- **Family Size**: Best survival with 2–4 members (55–72%). Alone passengers only ~30%.  
- **Tickets**: Shared tickets → 51.8% survival vs 29.8% for individual.  
- **Cabins**: Decks B, D, E had >70% survival.  
- **Embarked**: Cherbourg (C) passengers had higher rates.  

---

## 📈 Visuals
- Survival distribution (pie chart)  
- Count & bar plots (Sex, Pclass, Embarked, etc.)  
- Age & Fare histograms  
- KDE plots (age × gender × survival)  
- Boxplots (fare outliers)  
- Survival by Title, Ticket, Cabin, Family  

---

## 🔍 Findings
- Women & children prioritized.  
- Higher class → higher chance of survival.  
- Ticket type & cabin location linked to socio-economic status & survival.  
- Being with family improved survival chances.  


