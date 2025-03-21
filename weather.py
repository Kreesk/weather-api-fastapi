import httpx
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


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