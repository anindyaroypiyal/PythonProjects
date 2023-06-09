import requests

API_KEY = '0d221781bc99929222e57e8beabb94bb'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    tempa = round(data['main']['temp'] - 273.15 , 2)
    print("Weather:",weather)
    print("Temparature is",tempa,"℃")
else:
    print("An error occured.")