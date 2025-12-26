import os
from google.genai import types

def get_file_content(working_directory, file_path="."):
    file_path = os.path.join(working_directory, file_path)
    abs_working = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(abs_working):
        return (
            f'Error: Cannot read "{file_path}" as it ' 
            'is outside the permitted working directory'
        )
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file "{file_path}"'
    MAX_CHARS = 10000

    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    return file_path, file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the file path and contents of a file up to 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read data from, "
                    "file relative to the working directory "
                    "(default is the working directory itself)",
            ),
        },
        required=['file_path']
    ),
)
