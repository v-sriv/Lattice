# Google - GenAI Dependency: To call the Gemini LLM
# Python-dotenv Dependency: To load the .env file to the process
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
MODEL  = "gemini-3.8-flash"

running_status = True
last_interaction_id = ""

while(running_status):
    prompt = input("User: ")

    if prompt == "/quit":
        running_status = False
        break

    interaction = client.interactions.create(
        model = MODEL,
        input = prompt, # Prompt
        stream = True,
        previous_interaction_id = last_interaction_id
    )

    # print(f"Output: {interaction.output_text}")
    for event in interaction:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end = "", flush = True)
        elif event.event_type == "interaction.completed":
            last_interaction_id = event.interaction.id            

    print("\n---------------------\n")