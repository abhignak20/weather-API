import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "4b8476534211bb1757d5295261af4ab7"
CITY = "Hyderabad"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

weather_data = {
    "Metric": ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"],
    "Value": [temperature, humidity, pressure]
}

df = pd.DataFrame(weather_data)

plt.bar(df["Metric"], df["Value"])
plt.title("Weather Data Visualization")
plt.xlabel("Weather Metrics")
plt.ylabel("Values")
plt.savefig("weather_dashboard.png")
plt.show()

