import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(target_dir) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    max_chars = 10000
    try:
        with open(target_dir, 'r') as file:
            file_string = file.read(max_chars)
    except Exception as e:
        return f"Error: {e}"
    if len(file_string) == 10000:
        return f'{file_string} "{file_path}" truncated at 10000 characters'
    return file_string

