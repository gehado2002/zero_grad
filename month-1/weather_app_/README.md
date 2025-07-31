# 🌤️ Weather App – OpenWeatherMap API

A simple Python program that fetches **real-time weather data** for any city using the [OpenWeatherMap API](https://openweathermap.org/api).  
It displays temperature, humidity, pressure, and more in a **clean table format** using `pandas`.

---

## 📌 Features
✅ Fetches **real-time weather data** using OpenWeatherMap API  
✅ Displays results in a **neat table (DataFrame)**  
✅ Provides **city validation** (handles wrong city names)  
✅ Allows users to **search for multiple cities in a single run**  

---

## 🎯 How It Works
1️⃣ The user enters a **city name**.  
2️⃣ The program fetches data from OpenWeatherMap API.  
3️⃣ Weather parameters (temp, humidity, pressure, etc.) are displayed in a table.  
4️⃣ The user can **try again** or exit.  

---

## 📸 Example Output
```
enter the city name : cairo

🌤️ Weather in Cairo 🌤️

Parameter Value
temp 32.42
feels_like 34.65
temp_min 31.90
temp_max 32.42
pressure 1005.00
humidity 48.00
sea_level 1005.00
grnd_level 1000.00

try again 🤷‍♀️? "y/n"y

enter another city name : t
city t is not found 😔
```
## Feel free to fork, modify, and enhance the project! 💡
