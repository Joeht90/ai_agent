import os

def write_file(working_directory, file_path, content):
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
    return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

