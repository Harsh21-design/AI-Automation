import requests

url = "http://127.0.0.1:5000/secure"
headers = {"Authorization": "Bearer mysecretkey123"}

response = requests.get(url, headers=headers)
print(response.json())
