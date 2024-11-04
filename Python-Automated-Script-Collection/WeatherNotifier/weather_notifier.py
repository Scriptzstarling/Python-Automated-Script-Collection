import requests

def get_weather(city_name):
    api_key = "d0091b301005155fdef2cab6c916ac44"  # Replace with your actual OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city_name}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found, please try again.")

# Prompt user for the city name
city_name = input("Enter the name of the city: ")
get_weather(city_name)
