import os
import sys
from dotenv import load_dotenv
from camel.types import ModelPlatformType
from camel.configs import OpenRouterConfig
from utils.wei_utils import get_agent_config

# Load environment variables from .env file
load_dotenv()

# Create a custom model configuration for OpenRouter with GPT-4o-mini
def get_custom_openrouter_config():
    agent_config = {
        'model_type': "openai/gpt-4o-mini",  # OpenRouter path to GPT-4o-mini
        'model_platform': ModelPlatformType.OPENROUTER,
        'model_config': OpenRouterConfig().as_dict(),
    }
    return agent_config

if __name__ == "__main__":
    # Check if we have the required environment variables
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable is not set.")
        sys.exit(1)
    
    # Get the paper path from command line arguments
    if len(sys.argv) < 2:
        print("Usage: python custom_openrouter.py <path_to_paper.pdf>")
        sys.exit(1)
    
    paper_path = sys.argv[1]
    
    # Run the poster generation pipeline with our custom configuration
    cmd = f"""
    python -m PosterAgent.new_pipeline \
        --poster_path="{paper_path}" \
        --model_name_t="openai/gpt-4o-mini" \
        --model_name_v="openai/gpt-4o-mini" \
        --poster_width_inches=48 \
        --poster_height_inches=36
    """
    
    print(f"Running command: {cmd}")
    os.system(cmd)