import requests
import matplotlib.pyplot as plt
from datetime import datetime

# ✅ Your API Key
API_KEY = '030907ab1fd0812fde1107af02076ed8'

# 🔍 Ask user for city name
city = input("Enter your city name: ")

# 📡 Make request to OpenWeatherMap API (5 day forecast every 3 hours)
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# 🛑 Error check
if data.get("cod") != "200":
    print("Error fetching data:", data.get("message"))
    exit()

# 📊 Extract datetime & temperature
dates = []
temperatures = []

for item in data["list"]:
    # Convert timestamp to readable time
    time = datetime.fromtimestamp(item["dt"])
    temp = item["main"]["temp"]

    dates.append(time)
    temperatures.append(temp)

# 📈 Plotting
plt.figure(figsize=(12, 6))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='skyblue')

plt.title(f"Temperature Forecast for {city}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
