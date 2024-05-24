#!/usr/bin/python3

import requests

# API endpoint URL
url = "https://api.sampleapis.com/recipes/recipes"

# Send GET request
response = requests.get(url)

# Check if request was successful (status code 200)
if response.status_code == 200:
    #convert JSON response to python dictionary
    data = response.json()

    print(data)
else:
    print("ERROR: ", response.status_code)
