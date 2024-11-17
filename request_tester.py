import requests

url = "http://127.0.0.1:8000/calculate-stats/"
data = {"data_input": [1, 2, 3, 4, 5]}

response = requests.post(url, json=data)

print(response.json())