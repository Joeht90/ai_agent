import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt as system_prompt
from call_function import available_functions, call_function

MAX_ITERS = 20

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
    for _ in range(MAX_ITERS):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash', 
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt),
            )
            for candidate in response.candidates:
                messages.append(candidate.content)
            if not response.usage_metadata:
                raise RuntimeError("Gemini API response appears to be malformed")
            if args.verbose == True:
                print(
                    f"User prompt: {args.user_prompt}\n"
                    f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
                    f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
                )
            if response.function_calls:
                function_responses = []
                for function_call in response.function_calls:
                    result = call_function(function_call, args.verbose)
                    if (
                        not result.parts
                        or not result.parts[0].function_response
                        or not result.parts[0].function_response.response
                    ):
                        raise RuntimeError(f"Empty function response for {function_call.name}")
                    if args.verbose:
                        print(f"-> {result.parts[0].function_response.response}")
                    function_responses.append(result.parts[0])
                messages.append(types.Content(parts=function_responses, role="user"))
            else:
                if response.text:
                    print(
                        f'{response.text}'
                    )
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
