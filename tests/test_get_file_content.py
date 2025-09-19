from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def main():
    load_dotenv()
    working_dir = "calculator"
    #print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "/bin/cat"))
    print(get_file_content(working_dir, "pkg/does_not_exist.py"))

main()