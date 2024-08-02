from django.test import TestCase
import requests
import json

class Test(TestCase):
    url1 = "http://localhost:8008/api/v1/bloglist/"
    # payload1 - для POST
    # payload2 - для PATCH
    payload1 = {"title":"Hello python any", "content":"any", "is_published":"true"}
    payload2 = {"title":"Hello mister"}
    json_payload1 = json.dumps(payload1, indent = 4)
    json_payload2 = json.dumps(payload2, indent = 4)
    headers12 = {"Authorization":"Basic YWRtaW46YWRtaW4=", 'Content-Type': 'application/json'}
    url2 = "will be in POST-method with special ID"

    def setUp(self):
        print("##########")
        print("Initial setup:")
        print('1) read a list of all')
        print('2) create an object - so we got an ID')
        print('3) change this object with ID')
        print('4) delete this object with ID')
        print("##########")

    def test_GET_POST_PATCH_DELETE(self):
        print("##########")
        print("test_GET:")
        response = requests.request("GET", self.url1, headers=self.headers12, data={})
        print(response.text)
        self.assertEqual(response.status_code, 200)
        print("##########")
        
        print("##########")
        print("test_POST:")
        response = requests.request("POST", self.url1, headers=self.headers12, data=self.json_payload1)
        jsonString= response.text
        dictionary = json.loads(jsonString)
        print(dictionary)
        #########
        ID = str(dictionary['post']['id'])
        print("\n id = " + ID)
        self.url2 = "http://localhost:8008/api/v1/bloglist/"+ID+"/"
        #########
        self.assertEqual(response.status_code, 201)
        print("##########")
        
        print("##########")
        print("test_PATCH:")
        response = requests.request("PATCH", self.url2, headers=self.headers12, data=self.json_payload2)
        print(response.text)
        self.assertEqual(response.status_code, 202)
        print("##########")

        print("##########")
        print("test_DELETE:")
        response = requests.request("DELETE", self.url2, headers=self.headers12, data={})
        print(response.text)
        self.assertEqual(response.status_code, 200)
        print("##########")
        
