import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working = os.path.abspath(working_directory)
        command_list = ["python3", target_path]
        for i in args:
            command_list.append(i)
        if not target_path.startswith(abs_working):
            return(
            f'Error: Cannot execute "{file_path}" as it '
            'is outside the permitted working directory'
            )
        if not os.path.exists(target_path):
            return(f'Error: File "{file_path}" does not exist.')
        if not file_path.endswith(".py"):
            return(f'Error: "{file_path}" is not a Python file.')
        result = subprocess.run(command_list, timeout=30, capture_output=True, text=True)
        if result.stdout != 0:
            return f"Process exited with code STDOUT: {result.stdout} STDERR: {result.stderr}"
        if result.stdout == Null and result.stderr == Null:
            return "No output produce"
        return f"Process completed. STDOUT: {result.stdout} STDERR: {result.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

