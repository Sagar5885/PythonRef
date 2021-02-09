import requests
import json
import jsonpath

#API URL
url = "http://reqres.in/api/users?page=2"

#Send Get Request
response = requests.get(url)
print(response)

#Display Response Content
print(response.content)
print(response.headers)
print()

#parse response to json format
json_response = json.loads(response.text)
print(json_response)
print()

#Fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
assert pages[0] == 2
print(pages[0])