import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    file_path = os.path.join(working_directory, directory)
    abs_working = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, directory))
    if not target_path.startswith(abs_working):
        return (
            f'Error: Cannot list "{directory}" as it ' 
            'is outside the permitted working directory'
        )
    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
    file_list = os.listdir(target_path)
    return_list = []
    for name in file_list:
        full_path = os.path.join(target_path, name)
        size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)

        line = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
        return_list.append(line)

    return "\n".join(return_list)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative "
        "to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, " 
                "relative to the working directory "
                "(default is the working directory itself)",
            ),
        },
    ),
)
