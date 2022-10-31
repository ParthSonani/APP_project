import requests
import json

def tackle_data_from_api():
    response_of_api = requests.get('https://api.nytimes.com/svc/movies/v2/critics/all.json')
    print(response_of_api)
    data =response_of_api.text

# Press the green button in the gutter to run the script.
tackle_data_from_api()