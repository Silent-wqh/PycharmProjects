filename = 'PythonStudyNotes.txt'
with open(filename, encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
with open(filename, encoding='utf-8') as file_object:
    print('*' * 40)
    for line in file_object:
        print(line.rstrip())
    print('*' * 40)
with open(filename, encoding='utf-8') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
