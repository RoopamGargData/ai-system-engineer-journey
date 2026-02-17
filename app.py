from fastapi import FastAPI
from utils import get_joke_safe, load_config

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI System Engineer Server Running"}

@app.get("/joke")  #API route define
def joke():    #route handler function
    result = get_joke_safe()    #safe function call
    return {"joke": result}   #JSON response result


@app.get("/config")
def config():
    return load_config()