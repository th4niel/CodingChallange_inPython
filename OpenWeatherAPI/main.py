import requests

OWA = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c0bec81957710a8db55e7a9c528aefb3"


data_weather = {
    "lat": -6.175110,
    "lon": 106.865036,
    "appid": api_key,
}

response = requests.get(OWA, params=data_weather)
print(response.json())