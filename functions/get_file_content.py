import os


def get_file_content(working_directory, file_path):
    # Get the absolute path of the working directory
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    # If a file_path is provided, join it with the working directory to get the target file's absolute path
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    # Prevent access to files outside the working directory
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    # Check if the target path is a regular file
    if os.path.isfile(target_dir) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    max_chars = 10000  # Limit the number of characters to read
    try:
        # Try to open and read up to max_chars from the file
        with open(target_dir, 'r') as file:
            file_string = file.read(max_chars)
    except Exception as e:
        # Return an error message if reading fails
        return f"Error: {e}"
    # If the file is longer than max_chars, indicate truncation
    if len(file_string) == 10000:
        return f'{file_string} "{file_path}" truncated at 10000 characters'
    # Return the file content
    return file_string

