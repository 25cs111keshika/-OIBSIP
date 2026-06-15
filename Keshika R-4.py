import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")

city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    data = requests.get(url, timeout=5).json()

    if data["cod"] == 200:
        print("\n--- Weather Report ---")
        print("City       :", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like :", data["main"]["feels_like"], "°C")
        print("Humidity   :", data["main"]["humidity"], "%")
        print("Condition  :", data["weather"][0]["description"])
        print("Wind Speed :", data["wind"]["speed"], "m/s")
    elif data["cod"] == 404:
        print("City not found!")
    elif data["cod"] == 401:
        print("Invalid API key!")

except requests.exceptions.ConnectionError:
    print("No internet connection!")
except requests.exceptions.Timeout:
    print("Request timed out!")