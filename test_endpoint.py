import requests

Endpoint = "http://api.aviationstack.com/v1/flights?access_key=7838e177f2ab9fddc1dbf077cb72708e"

#Testing function
def test_endpoint():
    response = requests.get(Endpoint)
    print(response)
    if response.status_code != 200:
        print("wrong status code" + response.status_code)
    assert response.status_code == 200


test_endpoint()