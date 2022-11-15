import requests
import unittest
from connection import Connection

Endpoint = "http://api.aviationstack.com/v1/flights?access_key=7838e177f2ab9fddc1dbf077cb72708e"


class TestApp(unittest.TestCase):
    def test_get_connection(self):
        self.assertEqual(Connection.get_connection(), Connection.conn)

#Testing function
    def test_endpoint(self):
        response = requests.get(Endpoint)
        print(response)
        if response.status_code != 200:
            print("wrong status code" + response.status_code)
        assert response.status_code == 200


