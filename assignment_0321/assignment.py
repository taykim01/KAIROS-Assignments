from dotenv import load_dotenv
from get_current_weather import get_current_weather
from getAIResponse import getAIResponse
from get_plain_ai_response import get_plain_ai_response
import json
load_dotenv()


# enter the location and format of the weather in chat
# extract the location and format informatio
# make the function call to get_current_weather
# reply the chat data with the weather information


user_input = input("Enter a message(i.e. ask about a city's weather): ")
ai_response = getAIResponse("From the user's response: '" + user_input + "', extract the city and the format. Return the city and the format in the following format, which is a JSON format: ['city': city name, 'format': format name]. Format name should be in metric or imperial.")

if ai_response is not None:
    weather_query = json.loads(ai_response)
    location = weather_query["city"]
    format = weather_query["format"]
else:
    print("Error: Invalid response. Please try again.")
weather = get_current_weather(location, format)
weather_response = get_plain_ai_response("The weather in " + location + " is: temperature: " + str(weather["temperature"]) + " degrees, humidity: " + str(weather["humidity"]) + ", description: " + str(weather["description"]) + ". Explain the weather in " + location + " as if you are a weather forecaster. Use the " + format + " system.")
print(weather_response)