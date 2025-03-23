import httpx
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"



async def get_current_weather(city: str) -> dict:
    async with httpx.AsyncClient() as client:
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"}
        response = await client.get(BASE_URL, params=params)
        if response.status_code != 200:
            raise ValueError("Город не найден или ошибка API")
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }

async def get_weather_forecast(city: str) -> dict:
    async with httpx.AsyncClient() as client:
        params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"}
        response = await client.get(FORECAST_URL, params=params)

        if response.status_code != 200:
            raise ValueError(f"Ошибка API: {response.status_code} - {response.text}")

        data = response.json()
        if "list" not in data or not data["list"]:
            raise ValueError("Данные прогноза не найдены в ответе API")

        forecast_list = []
        for entry in data['list'][::8]:
            forecast_list.append({
                "city": data["city"]["name"],
                "temperature": entry["main"]["temp"],
                "description": entry["weather"][0]["description"],
                "humidity": entry["main"]["humidity"]
            })
        return {"city": data["city"]["name"], "forecast": forecast_list[:5]}