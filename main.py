# Google - GenAI Dependency: To call the Gemini LLM
# Python-dotenv Dependency: To load the .env file to the process
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
MODEL  = "gemini-3.8-flash"

running_status = True

while(running_status):
    prompt = input("User: ")

    if prompt == "/quit":
        running_status = False
        break

    interaction = client.interactions.create(
        model = MODEL,
        input = prompt # Prompt
    )

    print(f"Output: {interaction.output_text}")
    print("---------------------\n")

