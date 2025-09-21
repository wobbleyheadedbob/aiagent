import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    #If the file_path is outside the working directory, return a string with an error:
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    #If the file_path doesn't exist, return an error string:
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    #If the file doesn't end with ".py", return an error string:
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    #If any exceptions occur during execution, catch them and return an error string:
    try:
        final_args = ["python3",file_path]
        final_args.extend(args)

        output = subprocess.run(
            final_args,
            cwd=abs_working_directory,
            timeout=30,
            capture_output=True
        )
        final_string = f"""
STDOUT: {output.stdout}
STDERR: {output.stderr}
"""
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        if output.returncode != 0:
            final_string += f'Process exited with code {output.returncode}'
        return final_string
    except Exception as e:
        return f"Error: executing Python file: {e}"