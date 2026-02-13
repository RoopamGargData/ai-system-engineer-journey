from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI System Engineer Server Running"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"greet": f"Hello {name}, welcome to AI Engineering"}