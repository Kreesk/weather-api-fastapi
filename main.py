from fastapi import FastAPI, HTTPException
from models import WeatherResponse, ForecastResponse
from weather import get_current_weather, get_weather_forecast

app = FastAPI(title="Weather API", description="API для получения погоды")

@app.get("/weather/", response_model=WeatherResponse)
async def weather(city: str):
    try:
        return await get_current_weather(city)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/weather/forecast/", response_model=ForecastResponse)
async def forecast(city: str):
    try:
        return await get_weather_forecast(city)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
