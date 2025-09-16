from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"
    #print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

main()