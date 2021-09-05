while(1):
    try:
        num1 = int(input('输入1号数字：'))
        num2 = int(input('输入2号数字：'))
    except TypeError:
        print('请输入数字')
    except ValueError:
        print('请输入数字')
    else:
        print(num1 + num2)