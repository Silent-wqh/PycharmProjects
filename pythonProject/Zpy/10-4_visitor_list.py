names = []
with open('guest_book.txt', 'w') as file_object:
    while(1):
        name = input('请输入名字：')
        if name != 'quit':
            file_object.write(f'{name}\n')
            print(f'你好{name}')
        else:
            break
