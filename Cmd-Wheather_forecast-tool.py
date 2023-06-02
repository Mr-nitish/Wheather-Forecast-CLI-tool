import requests     # Importing the requests library to make HTTP requests
import json     # Importing the json library to parse JSON responses
import sys    # Importing the sys module for system-specific parameters and functions

def get_weather(city):
    api_key = "c8ffd212947508eaeea2414db5b2b967"  # Replace with your OpenWeatherMap API key

     # Constructing the URL to make the API request, including the city name and API key   
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)  # Sending an HTTP GET request to the OpenWeatherMap API
        response.raise_for_status()  # Checking for any HTTP errors
        weather_data = json.loads(response.text)  # Parsing the JSON response into a Python dictionary
        return weather_data  # Returning the weather data
   
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)  # Exiting the program with a non-zero status code if an HTTP error occurs
   
    except Exception as err:
    except Exception as err:
        print(f"An error occurred: {err}")
        sys.exit(1)   # Exiting the program with a non-zero status code if any other error occurs

def parse_weather(weather_data):
    
    # Extracting the required weather information from the weather data dictionary
    weather = weather_data["weather"][0]["main"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    return weather, temperature, humidity, wind_speed    # Returning the extracted weather information

def print_weather(city, weather, temperature, humidity, wind_speed):
   
    # Printing the weather forecast information
    print(f"Weather forecast for {city}:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the name of a city as an argument.")
        sys.exit(1)   # Exiting the program with a non-zero status code if the number of arguments is incorrect

    city = sys.argv[1]  # Retrieving the city name from the command-line argument
    weather_data = get_weather(city)    # Calling the get_weather function to fetch weather data

    if weather_data is not None:   # Checking if weather data was successfully retrieved
      
        # Parsing the weather data into individual variables
        weather, temperature, humidity, wind_speed = parse_weather(weather_data)
       
        # Printing the weather forecast
        print_weather(city, weather, temperature, humidity, wind_speed)
