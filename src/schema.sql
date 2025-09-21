DROP TABLE IF EXISTS weather_records;

CREATE TABLE weather_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    temperature TEXT NOT NULL,
    raw TEXT,
    humidity INTEGER ,
    feels_like_t FLOAT,
    summary TEXT,
    alerts TEXT
);
