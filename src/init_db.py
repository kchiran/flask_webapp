import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO weather_records (city, temperature, humidity) VALUES (?, ?, ?)",
            ('Seattle', 12, 15)
            )

cur.execute("INSERT INTO weather_records (city, temperature, humidity) VALUES (?, ?, ?)",
            ('Dallas', 13, 16)
            )

connection.commit()
connection.close()
