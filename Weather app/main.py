import requests

API_KEY = "13f2758c7de51fc00a34e006cb57db12" #USe Your own API KEY
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")
url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    main = data["main"]
    temperature = main["temp"]
    humidity = main["humidity"]
    weather = data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather}")
else:
    print("City not found!")
