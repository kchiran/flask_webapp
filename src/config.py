#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Weather.sqlite3'
