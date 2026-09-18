import requests
import pymysql

# This URL asks for Bangalore's current weather - no signup needed
url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current_weather=true"

response = requests.get(url)   # STEP 1: EXTRACT - actually go fetch the data
data = response.json()          # convert the response into a Python dictionary

print("Raw response:")
print(data)

current = data["current_weather"] 

print("\n--- Just what we need ---")
print("Temperature:", current["temperature"], "°C")
print("Windspeed:", current["windspeed"], "km/h")
print("Time:", current["time"])
print("winddirection:", current["winddirection"])



connection = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",   
    database="de_practice"
)

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO weather_log (temperature, windspeed, winddirection, recorded_time) VALUES (%s, %s, %s, %s)",
    (current["temperature"], current["windspeed"], current["winddirection"], current["time"])
)

connection.commit()
connection.close()

print("\nSaved to database!")