from fastapi import FastAPI
from services.weather_service import get_current_weather, get_forecast_weather

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Weather App!"}

@app.get("/weather/current")
def current_weather(city: str):
    return get_current_weather(city)

@app.get("/weather/forecast")
def forecast_weather(city: str):
    return get_forecast_weather(city)