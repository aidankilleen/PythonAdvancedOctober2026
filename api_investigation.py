# api_investigation.py

import requests

url = "https://api.acodingtutor.com/users/1082?_delay=5000"


# synchronous call
response = requests.get(url)

data = response.json()

print(data)

print ("finished")




