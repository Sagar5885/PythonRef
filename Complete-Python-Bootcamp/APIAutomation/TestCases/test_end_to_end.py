import requests
import json
import jsonpath

def test_Add_new_data():
    App_URL = "http://reqres.in/api/users"
    file = open("/Users/hiralsuthar1/Project/PythonRef/Complete-Python-Bootcamp/APIAutomation/Resources/create1.json")
    requests_json = json.loads(file.read())
    response = requests.post(App_URL, requests_json)
    print(response.text)