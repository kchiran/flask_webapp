import os
import requests

# Example uses OpenWeatherMap current weather API. Configure via WEATHER_API_KEY env var.
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def fetch_current_weather(city: str, api_key: str = None):
    api_key = api_key or os.getenv('WEATHER_API_KEY')
    if not api_key:
        raise RuntimeError('WEATHER_API_KEY not configured')

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    resp = requests.get(BASE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
