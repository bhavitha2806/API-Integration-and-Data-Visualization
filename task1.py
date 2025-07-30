import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your actual API key
API_KEY = "071c59c4e25cdccf8a41c6ef6c42c03c"
CITY = "Chennai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    """Fetch weather forecast data from OpenWeatherMap API."""
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from OpenWeatherMap API. Check your API key or city name.")

def parse_data(data):
    """Parse temperature and time data from the API response."""
    temps = []
    times = []
    for entry in data['list']:
        temps.append(entry['main']['temp'])
        times.append(datetime.fromtimestamp(entry['dt']))
    return times, temps

def visualize_data(times, temps):
    """Visualize temperature forecast data using matplotlib."""
    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o', linestyle='-', color='blue')
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("weather_forecast.png")
    plt.show()

def main():
    data = fetch_weather_data()
    times, temps = parse_data(data)
    visualize_data(times, temps)

if __name__ == "__main__":
    main()
