import requests 

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    res = requests.get(url)
    data = res.json()

    joke = data["setup"] + "  - " + data["punchline"]
    return joke