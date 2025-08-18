import sys
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    try: 
        input_argument = sys.argv[1]
        print("Hello from aiagent!")
        response = client.models.generate_content(model = "gemini-2.0-flash-001",contents = input_argument)
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count }")

    except Exception:
        print ("Usage: python3 main.py <input_argument>")
        sys.exit(1)

if __name__ == "__main__":
    main()
