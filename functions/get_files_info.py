from pathlib import Path

def get_files_info(working_directory, directory=None):
    if directory not in working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not directory.is_dir():
        return f'Error: "{directory}" is not a directory'



