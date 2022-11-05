import requests
import json

params = {
  'access_key': '7838e177f2ab9fddc1dbf077cb72708e'
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()
print (api_response)

# Downloading json data into a file
data = json.dumps(api_response)
file = open("data.json","w")
file.write(data)
print("API data successfully downloaded!!")
