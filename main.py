import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv
from config import system_prompt
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={    
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("user_input")
    parser.add_argument(
        "--verbose", action="store_true", 
        help="Enable verbose output"
        )
    args = parser.parse_args()
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=args.user_input,
        config=types.GenerateContentConfig(
             tools=[available_functions], system_instruction=system_prompt),
        )

    if response.function_calls != []:
        print(f"Calling function: {response.function_calls[-1].name}({response.function_calls[-1].args})")
    else:
        print(response.text)
    if args.verbose:
          print(f"User prompt: {args.user_input}\n" +
          f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n" +
          "Response tokens: ", response.usage_metadata.canidates_token_count
          )


main(sys.argv)
