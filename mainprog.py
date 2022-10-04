import requests
import API

url = 'api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=86ca0c546eb8716872e0bb0463df31d6'


r = requests.get(url)

print(r.status_code)