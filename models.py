from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float  # Температура в градусах Цельсия
    description: str   # Описание погоды (например, "ясно")
    humidity: int      # Влажность в процентах