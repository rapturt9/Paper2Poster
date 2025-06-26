import os
import sys
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the OpenRouter API key
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if not openrouter_api_key:
    print("Error: OPENROUTER_API_KEY environment variable is not set.")
    sys.exit(1)

def call_openrouter_api(pdf_text):
    """Call the OpenRouter API with GPT-4o-mini to generate poster content."""
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://all-hands.dev",
        "X-Title": "Paper2Poster"
    }
    
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system", 
                "content": "You are an expert at creating academic posters from research papers. Extract the key information and organize it into a clear, visually appealing academic poster structure."
            },
            {
                "role": "user", 
                "content": f"Create an academic poster from this research paper. Extract the title, authors, abstract, introduction, methodology, results, and conclusion. Format it as a JSON with the following structure: {{\"title\": \"\", \"authors\": \"\", \"abstract\": \"\", \"introduction\": \"\", \"methodology\": \"\", \"results\": \"\", \"conclusion\": \"\", \"references\": \"\"}}. Here's the paper content:\n\n{pdf_text}"
            }
        ],
        "max_tokens": 2000,
        "response_format": {"type": "json_object"}
    }
    
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        return content
    else:
        print(f"Error calling OpenRouter API: {response.status_code}")
        print(response.text)
        return None

# Read the PDF text from a file
with open("dataset/paper/paper.txt", "r") as f:
    pdf_text = f.read()

# Call the API
content = call_openrouter_api(pdf_text)

# Save the JSON content to a file
if content:
    with open("poster_content.json", "w") as f:
        f.write(content)
    print("Content saved to poster_content.json")
    
    # Also print the parsed content
    try:
        data = json.loads(content)
        print("\nPoster Content:")
        print(f"Title: {data['title']}")
        print(f"Authors: {data['authors']}")
        print(f"Abstract: {data['abstract'][:100]}...")
    except json.JSONDecodeError:
        print("Error: Could not parse JSON content")
else:
    print("Error: No content generated")