# 🌦️ Weather App with FastAPI

A simple weather application built using **FastAPI** and **OpenWeather API** to fetch current and forecast weather data.

---

## 📦 Features:
- Get current weather information.
- Get 5-day weather forecast.
- Built with Python 3 and FastAPI.
- Easy-to-use RESTful API with Swagger UI.

---

## 🚀 Technologies Used:
- **Python 3**
- **FastAPI**
- **Uvicorn**
- **Requests**
- **python-dotenv**
- **OpenWeather API**

---

## 📦 Project Structure:
```plaintext
weather-app/
├── main.py                   # Main FastAPI server
├── services/
│   └── weather_service.py    # Weather API integration logic
├── tests/
│   └── test_api.py           # Basic test cases
├── .env                      # API Key (excluded from Git)
├── .gitignore                # Ignore unnecessary files
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation