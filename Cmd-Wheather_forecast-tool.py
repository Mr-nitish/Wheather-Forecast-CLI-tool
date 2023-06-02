import requests
import json
import sys

def get_weather(city):
    api_key = "c8ffd212947508eaeea2414db5b2b967"  # Replace with your OpenWeatherMap API key

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = json.loads(response.text)
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)
    except Exception as err:
        print(f"An error occurred: {err}")
        sys.exit(1)

def parse_weather(weather_data):
    weather = weather_data["weather"][0]["main"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    return weather, temperature, humidity, wind_speed

def print_weather(city, weather, temperature, humidity, wind_speed):
    print(f"Weather forecast for {city}:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the name of a city as an argument.")
        sys.exit(1)

    city = sys.argv[1]
    weather_data = get_weather(city)

    if weather_data is not None:
        weather, temperature, humidity, wind_speed = parse_weather(weather_data)
        print_weather(city, weather, temperature, humidity, wind_speed)
