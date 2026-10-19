import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from google import genai
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

client = genai.Client()
MODEL  = "gemini-3.8-flash"

# Listens for POST request on "/chat" and sends a response back
@app.post("/chat")
async def chat(request: Request):

    user_message = await request.body()

    interaction = client.interactions.create(
        model = MODEL,
        input = user_message,
    )
    output = interaction.output_text

    return output

# This is to serve the frontend files at the "/" route
app.mount("/", StaticFiles(directory="front-end", html=True), name="frontend")