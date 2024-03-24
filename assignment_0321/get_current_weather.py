import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ.get("WEATHER_API_KEY")

def get_current_weather(location, format):
    api_key = API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}appid={api_key}&q={location}&units={format}"

    response = requests.get(complete_url)

    print(response)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
        return weather_data
    else:
        return response.status_code