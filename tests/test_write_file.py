from functions.write_file import write_file


def main():
    working_dir = "calculator"
    print(f'lorem.txt: {write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')
    #print(f'pkg/morelorem.txt: {write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
    #print(f'/tmp/temp.txt: {write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')


main()