import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt as system_prompt
from call_function import available_functions as available_functions

# Create gemini client and pass api_key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api_key wasn't found.  main.py ln 4-5")
client = genai.Client(api_key=api_key)

# create argument parser object
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


def main():
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    if args.verbose == True:
        print(
            f"User prompt: {args.user_prompt}\n"
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
            f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
        )
    if response.function_calls != None:
        for function_call in function_calls:
            print(
                f"calling function: {function_call.name}({function_call.args})"
            )
    else:
        print(
            f'{response.text}'
        )

if __name__ == "__main__":
    main()
