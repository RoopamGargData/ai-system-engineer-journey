import requests   #internet se data lene ke liye library
import json       
import logging    #system event record krne ke liye

logging.basicConfig(
    filename="app.log",
    level= logging.INFO,
    format="%(asctime)s - %(message)s"
)

def load_config():
    with open("config.json", "r") as f:
        data = json.load(f)
        return data

#def get_joke_safe():   #new safe function bna rahe (error handling karega)
    #try:   #risky code ko try block me rakhte hai
        #url = "https://official-joke-api.appspot.com/random_joke" #API address
        #res = requests.get(url, timeout=5) #request bhejna +5sec timelimit
        #data = res.json() #response ko python dict me convert 

    
        #joke = data["setup"] + "  - " + data["punchline"]  #fileds jod kar final text
        #logging.info("Joke fetched ok")  #sucess log karna 
        #return joke
    #except Exception as e:  #agar koi b error aaye to yha pakdo
       # logging.error(str(e))  #error log file me likho
       # return "No Joke available"  #crash ki jagah safe message do

def save_json_result(text):   #structured save function
    #dictonanry structure banana 
    data  ={"text" : text }  #key-value pair store
    
    with open("output.txt","a") as f:
        json.dump(data,f)   #json me convert karke write
        f.write(text + "\n")
    

def clean_text(text):    #reusable function bnani h text process krne k liye
    if not text:              #check agar empty input aaya
        return None
    text = text.strip()   #starting/ending space hatane ke liye
    text = text.lower()   #uniform format(processing easy)

    return text

