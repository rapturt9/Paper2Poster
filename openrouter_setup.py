import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenRouter API key
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if not openrouter_api_key:
    print("Error: OPENROUTER_API_KEY environment variable is not set.")
    sys.exit(1)

# Create a file to set the OpenAI API key to the OpenRouter API key
with open("/workspace/Paper2Poster/.env", "w") as f:
    f.write(f"OPENAI_API_KEY={openrouter_api_key}\n")
    f.write(f"OPENAI_API_BASE=https://openrouter.ai/api/v1\n")
    f.write(f"OPENROUTER_API_KEY={openrouter_api_key}\n")

print("OpenRouter API key has been set up as the OpenAI API key.")