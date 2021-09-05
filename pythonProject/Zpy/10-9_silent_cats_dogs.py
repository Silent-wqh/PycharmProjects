def print_file(filename):
    with open(filename) as file_object:
        contents = file_object.read()
        print(contents.rstrip())

try:
    print_file('cats..txt')
    print_file('dogs.txt')
except FileNotFoundError:
    pass