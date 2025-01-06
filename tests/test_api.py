from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_current_weather():
    response = client.get("/weather/current?city=Enschede")
    assert response.status_code == 200

def test_forecast_weather():
    response = client.get("/weather/forecast?city=Enschede")
    assert response.status_code == 200