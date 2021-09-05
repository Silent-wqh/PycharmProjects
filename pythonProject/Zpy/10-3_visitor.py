
name = input('输入名字：')

with open('guest.txt', 'w') as file_object:
    file_object.write(name)
