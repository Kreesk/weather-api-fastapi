from pydantic import BaseModel
from typing import List

class WeatherResponse(BaseModel):
    city: str
    temperature: float  # Температура в градусах Цельсия
    description: str   # Описание погоды (например, "ясно")
    humidity: int      # Влажность в процентах

class ForecastResponse(BaseModel):
    city : str
    forecast: List[WeatherResponse]