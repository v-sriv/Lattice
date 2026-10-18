from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Listens for POST request on "/chat" and sends a response back
@app.post("/chat")
def chat():
    print("Received.")
    return "Hello Chat!"

# This is to serve the frontend files at the "/" route
app.mount("/", StaticFiles(directory="front-end", html=True), name="frontend")