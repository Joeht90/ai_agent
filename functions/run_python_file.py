import os
import subprocess


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, full_path]) != abs_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    try:
        result = subprocess.run(['python3', file_path], capture_output=True, text=True, timeout=30, cwd=abs_working_dir)
        if result.returncode != 0:
            return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nProcess exited with code {result.returncode}'
        if result.stdout.strip() == '' and result.stderr.strip() == '':
            return 'No output produced.'
        return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out'
    except Exception as e:
        return f'Error: executing Python file: {e}'