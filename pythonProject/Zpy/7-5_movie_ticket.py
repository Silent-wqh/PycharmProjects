while True:
    age = int(input('请输入年龄：'))
    if age < 3:
        print('免费')
    elif age <= 12 and age > 3:
        print('10美元')
    else:
        print('15美元')