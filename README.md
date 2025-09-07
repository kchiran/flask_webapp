# Flask Weather Analytics App

### Requirements:
- Redis server running (for rq workers)
- Python 3.9+
- A weather API key (OpenWeatherMap recommended). 
- Set WEATHER_API_KEY env var.

### Install:
`$ python -m venv .venv`

`$ source .venv/bin/activate`

`$ pip install -r requirements.txt`

### Environment variables:
- `WEATHER_API_KEY : your weather API key`
- `WEATHER_CITY : default city (optional)`
- `DATABASE_URL : optional (default sqlite:///weather.db)`
- `REDIS_URL : redis://localhost:6379/`

### Run the app:
`$ export FLASK_APP=src/app.py`

`$ flask run`

Start the RQ worker (in separate terminal):

`$ python worker.py`

Fetch from the web UI (POST /fetch) or use Python to enqueue:
> `from tasks import enqueue_fetch_weather`

> `enqueue_fetch_weather('London')`

#### Run tests:

`$ pytest -q`

#### Notes:
- For production, configure proper secret key and production-ready DB.
