import tempfile
import os
from src.models import Weather
from flask import Flask


def test_model():
    weather = Weather()
    weather.city = "Fargo"
    weather.humidity = 15
    weather.temperature = 12
    weather.feels_like_t = 10
    assert "Fargo" == weather.city
    assert 15 == weather.humidity
    assert 12 == weather.temperature
    assert 10 == weather.feels_like_t


def test_model_to_dict():
    weather = Weather()
    weather.id = 1
    weather.city = "Fargo"
    weather.datetime = "2025-09-13 14:22:16"
    weather.humidity = 1
    weather.temperature = 1
    weather.raw = "raw_message"
    weather.feels_like_t = 1
    weather.summary = "test_summary"
    weather.alerts = "alert"
    test_dict = {
        "id": 1,
        "city": "Fargo",
        "datetime": "2025-09-13 14:22:16",
        "temperature": 1,
        "raw": "raw_message",
        "humidity": 1,
        "feels_like_t": 1,
        "summary": "test_summary",
        "alerts": "alert"
    }
    assert test_dict == weather.to_dict()