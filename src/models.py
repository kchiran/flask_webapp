#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

db = SQLAlchemy(app)

'''
Define the database model
that is used to store 
the temperature.
'''


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(128), nullable=False)
    datetime = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow())
    temperature = db.Column(db.Integer, nullable=False)
    raw = db.Column(db.JSON, nullable=False)  # original API payload
    humidity = db.Column(db.Integer, nullable=True)
    feels_like_t = db.Column(db.Float, nullable=True)
    summary = db.Column(db.String(256), nullable=True)
    alerts = db.Column(db.JSON, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "city": self.city,
            "datetime": self.fetched_at.isoformat(),
            "temperature": self.temperature_c,
            "raw": self.raw,
            "humidity": self.humidity,
            "feels_like_t": self.feels_like_c,
            "summary": self.summary,
            "alerts": self.alerts
        }