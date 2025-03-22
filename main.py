from fastapi import FastAPI, HTTPException
from models import WeatherResponse, ForecastResponse
from weather import get_current_weather, get_weather_forecast

app = FastAPI(title="Weather API", description="API для получения погоды")

@app.get("/weather/", response_model=WeatherResponse)
async def weather(city: str):
    try:
        weather_data = await get_current_weather(city)
        return weather_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/weather/forecast/", response_model=ForecastResponse)
async def forecast(city: str):
    try:
        forecast_data = await get_weather_forecast(city)
        return forecast_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
