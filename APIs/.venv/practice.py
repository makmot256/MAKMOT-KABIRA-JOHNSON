import requests
import pandas as pd
API_KEY = '48648cfb5a56993eecf0353a725a1261'
# Coordintes for 
# Latitude and longitude for Kampala
lat = 0.347596
lon = 32.582520

# Example of a GET request to retrieve weather data
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
