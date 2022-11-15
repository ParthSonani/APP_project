import requests
import json

class ApiCall:
  def acall(self):
    params = {
      'access_key': '7838e177f2ab9fddc1dbf077cb72708e'
    }

    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()
    api_data = json.dumps(api_response)
    new_data = json.loads(api_data)
    get_data = new_data['data']
    print(get_data)

    return get_data

  def download_api_data(self, get_data):
    # Downloading json data into a file
    data = json.dumps(get_data)
    file = open("data.json", "w")
    file.write(data)
    print("API data successfully downloaded!!")


api = ApiCall()
get_data = api.acall()
api.download_api_data(get_data)
