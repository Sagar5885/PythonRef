import requests
import json
import jsonpath

#API URL
url = "http://reqres.in/api/users"

def test_create_new_user():
    #Read input json file
    file = open("/Users/hiralsuthar1/Project/PythonRef/Complete-Python-Bootcamp/APIAutomation/Resources/create1.json")
    json_input = file.read()
    requests_json = json.loads(json_input)
    print(requests_json)
    response = requests.post(url, requests_json)
    print(response.content)
    assert response.status_code == 200

def test_create_other_user():
    #Read input json file
    file = open("/Users/hiralsuthar1/Project/PythonRef/Complete-Python-Bootcamp/APIAutomation/Resources/create1.json")
    json_input = file.read()
    requests_json = json.loads(json_input)
    print(requests_json)
    response = requests.post(url, requests_json)
    #Fetch Header
    print(response.headers.get('Content-Type'))
    #parse response to json format
    response_json = json.loads(response.text)
    #pick id using json path
    id = jsonpath.jsonpath(response_json, 'data')
    print(id[0])
    print(jsonpath.jsonpath(response_json, 'data[0].first_name')[0])