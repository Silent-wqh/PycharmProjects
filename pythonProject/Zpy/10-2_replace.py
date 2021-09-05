filename = 'PythonStudyNotes.txt'
with open(filename, encoding='utf-8') as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())
