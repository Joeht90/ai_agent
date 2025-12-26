import os 
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        file_path = os.path.join(working_directory, file_path)
        abs_working = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_path.startswith(abs_working):
            return (
                f'Error: Cannot write "{file_path}" as it ' 
                'is outside the permitted working directory'
            )

        if not os.path.exists(target_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
        return(f'Successfully wrote to "{file_path}" '
            f'({len(content)} characters written)')
    except Exception as e:
        f"Error: writing to file: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites or creates a new file relative to "
                "the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file we want to overwrite "
                "or create."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Information we want to overwrite "
                "or write to the file."
            ),
        },
        required=['file_path', 'content']
    ),
)
