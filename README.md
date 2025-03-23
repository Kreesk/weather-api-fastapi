# Weather API на FastAPI

Простое REST API для получения текущей погоды и прогноза на 5 дней, построенное на FastAPI с использованием OpenWeatherMap API.

## Описание
Этот проект создан в учебных целях для изучения разработки API на FastAPI. Он предоставляет два эндпоинта:
- **Текущая погода**: Возвращает данные о погоде (температура, описание, влажность) для указанного города.
- **Прогноз погоды**: Возвращает прогноз на 5 дней с интервалом в 1 день для указанного города.

Проект использует асинхронные запросы через `httpx` и валидацию данных с помощью `Pydantic`.

## Требования
- Python 3.8+
- Учетная запись OpenWeatherMap и API-ключ (получить можно [здесь](https://openweathermap.org/api))

## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Kreesk/weather-api-fastapi.git
   cd weather-api-fastapi
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Создайте файл `.env` в корне проекта и добавьте свой API-ключ:
   ```bash
   OPENWEATHER_API_KEY=ваш_ключ_здесь
   ```

## Запуск
Запустите приложение с помощью `uvicorn`:
```bash
uvicorn main:app --reload
```
API будет доступно по адресу 
```bash
http://127.0.0.1:8000.
```
## Эндпоинты
1. **GET /weather/**  
   - **Описание**: Получить текущую погоду для города.
   - **Параметры**: `city` (строка, название города, например, `Moscow`).
   - **Пример запроса**: `http://127.0.0.1:8000/weather/?city=Moscow`
   - **Пример ответа**:
   ```
     {
       "city": "Moscow",
       "temperature": 5.2,
       "description": "ясно",
       "humidity": 60
     }
   ```
2. **GET /weather/forecast/**  
   - **Описание**: Получить прогноз погоды на 5 дней.
   - **Параметры**: `city` (строка, название города, например, `Moscow`).
   - **Пример запроса**: `http://127.0.0.1:8000/weather/forecast/?city=Moscow`
   - **Пример ответа**:
```
     {
       "city": "Moscow",
       "forecast": [
         {
           "city": "Moscow",
           "temperature": 5.2,
           "description": "ясно",
           "humidity": 60
         },
         {
           "city": "Moscow",
           "temperature": 6.1,
           "description": "облачно",
           "humidity": 65
         }
       ]
     }
```
## Документация API
После запуска приложения откройте `http://127.0.0.1:8000/docs` для интерактивной документации Swagger.

## Зависимости
- `fastapi` — фреймворк для создания API.
- `httpx` — асинхронный HTTP-клиент.
- `pydantic` — валидация данных.
- `python-dotenv` — загрузка переменных окружения.
- `uvicorn` — ASGI-сервер для запуска приложения.

## Лицензия
Проект распространяется под лицензией MIT.
