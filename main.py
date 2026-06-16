import requests

API_KEY = "9fb92ec11ddc3e51addc1dffa9b550bd"  # Replace with your OpenWeatherMap API key

city = input("Enter city name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=metric"
)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city_name}, {country}")
    print("-" * 30)
    print(f"Temperature : {temperature}°C")
    print(f"Feels Like  : {feels_like}°C")
    print(f"Condition   : {weather.title()}")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")

else:
    print("Error:", response.status_code)
    print("City not found or API key is invalid.")