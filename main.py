import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("user_input")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=argv
        )

    print(f"{response.text}")
    if args.verbose:
          print(f"User prompt: {args.user_input}\n" +
          f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n" +
          "Response tokens: "
          )


main(sys.argv[1])
