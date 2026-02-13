from fastapi import FastAPI
from utils import get_joke

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI System Engineer Server Running"}

@app.get("/joke")
def joke():
    return {"joke": get_joke()}