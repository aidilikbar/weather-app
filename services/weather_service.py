import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_current_weather(city: str):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_forecast_weather(city: str):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()