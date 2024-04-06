import requests

response = requests.get("https://api.github.com/repos/wijamw/api-request")
print(response.json())
print(type(response.json()))
print(response.json()[0])