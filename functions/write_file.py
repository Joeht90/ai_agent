import os

def get_file_content(working_directory, file_path=".", content):
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

get_file_content("calculator", "lorem.txt", "wait this isn't lorem ipsum")

