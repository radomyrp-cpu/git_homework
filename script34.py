import sqlite3
import requests
from datetime import datetime
connection = sqlite3.connect("weather.db")
connection.execute("""
CREATE TABLE IF NOT EXISTS weather (
    date_time TEXT,
    temperature REAL)""")
url = "https://api.open-meteo.com/v1/forecast?latitude=48.45&longitude=34.98&current=temperature_2m"
response = requests.get(url)
data = response.json()
temperature = data["current"]["temperature_2m"]
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Температура:", temperature, "°C")
print("Дата і час:", date_time)
connection.execute(
    "INSERT INTO weather VALUES (?, ?)",
    (date_time, temperature))
connection.commit()
rows = connection.execute("SELECT * FROM weather").fetchall()
print("Дані з бази:")
for row in rows:
 print(row)
connection.close()