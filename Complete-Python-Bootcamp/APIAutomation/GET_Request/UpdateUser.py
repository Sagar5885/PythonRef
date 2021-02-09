import requests
import json
import jsonpath

#API URL
url = "http://reqres.in/api/users/2"

#Read input json file
file = open("/Users/hiralsuthar1/Project/PythonRef/Complete-Python-Bootcamp/APIAutomation/Resources/create1.json")
json_input = file.read()
requests_json = json.loads(json_input)
print(requests_json)

response = requests.put(url, requests_json)
print(response.content)

assert response.status_code == 200

#Fetch Header
print(response.headers.get('Content-Type'))

#parse response to json format
response_json = json.loads(response.text)

#pick id using json path
updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt[0])