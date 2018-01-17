import requests
from pprint import pprint

url = 'http://itemstoreread.stg0.itemstore.catdev.glb.prod.walmart.com/itemstore-item-read-app/services/product'

req_payload = "[{\"productId\":\"39GMFY3XKNKY\"}]"

headers = {'Content-Type': 'application/json',
           'requestContext': "{\"tenantId\": 0, \"localeId\": \"en_US\"}"}

response = requests.request("POST", url, data=req_payload, headers=headers)

print(response.text)