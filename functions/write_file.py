import os


def write_file(working_directory, file_path, content):
    """
    Write content to a file in the specified working directory.
    
    :param working_directory: The directory where the file will be created.
    :param file_path: The path of the file to write.
    :param content: The content to write into the file.
    """
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.join(abs_working_dir, file_path)
    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    try:
        with open(full_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'