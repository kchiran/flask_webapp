#!/usr/bin/env python3
import sqlite3

from flask import Flask, render_template
from metrics import setup_metrics

app = Flask(__name__)
setup_metrics(app)


def get_db_connection():
    conn = sqlite3.connect('src/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    records = conn.execute('SELECT * FROM weather_records').fetchall()
    conn.close()
    return render_template('index.html', records=records)
