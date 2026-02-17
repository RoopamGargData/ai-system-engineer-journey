import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open ("output.txt", "a") as f: 
        json.dump(data,f)
        f.write("\n")
