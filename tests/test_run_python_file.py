from functions.run_python_file import run_python_file


def main():
    working_dir = "calculator"
    print(f'(Test 1 - should print the calculator\'s usage instructions {run_python_file("calculator", "main.py")}')
    #print(f'(Test 2 - should run the calculator... which gives a kinda nasty rendered result) {run_python_file("calculator", "main.py", ["3 + 5"])}')
    #print(f'(Test 3 - Dunno what this does {run_python_file("calculator", "tests.py")}')
    #print(f'(Test 4 - this should return an error {run_python_file("calculator", "../main.py")}')
    #print(f'(Test 5 - this should return an error {run_python_file("calculator", "nonexistent.py")}')   


main()

