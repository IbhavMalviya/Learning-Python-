import requests
import json

url="https://hacker-news.firebaseio.com/v0/item/31353677.json"
r=requests.get(url)
print(f"Status code: {r.status_code}")

response_dict=r.json()
response_dict=json.dumps(response_dict,indent=4)
print(response_dict)