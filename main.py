# Google - GenAI Dependency: To call the Gemini LLM
# Python-dotenv Dependency: To load the .env file to the process
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
MODEL  = "gemini-3.8-flash"
prompt = "Hello!"

interaction = client.interactions.create(
    model = MODEL,
    input = prompt # Prompt
)

print(interaction.output_text)