import json


def get_new_favorite_number(sign_symbol=0, favorite_number=0):
    """
    获取最喜欢的数字，并存储到'favorite_number.json'文件中
    :return: 最喜欢的数字
    """
    while 1:
        try:
            if sign_symbol == 0:
                favorite_number = int(input('输入一个最喜欢的数字：'))
        except ValueError:
            print('请输入数字')
        except TypeError:
            print('请输入数字')
        else:
            with open('favorite_number.json', 'w') as j_obj:
                json.dump(favorite_number, j_obj)
            return favorite_number


def get_stored_favorite_number():
    """
    获取json数据
    :return: 返回json数据
    """
    try:
        with open('favorite_number.json') as j_obj:
            favorite_number = json.load(j_obj)
    except FileNotFoundError:
        favorite_number = get_new_favorite_number()
        return favorite_number
    except json.decoder.JSONDecodeError:
        print('原数据文件错误，请手动修正')
    else:
        return favorite_number


def check_number():
    number = input('数字是否正确，若正确输入‘Yes’；'
                   '若不正确，请输入正确的数字：')
    while 1:
        if number != 'Yes' and number.isdigit():
            while 1:
                try:
                    number = int(number)
                except ValueError:
                    print('请输入正确的数字或‘Yes’')
                else:
                    get_new_favorite_number(1, number)
                    print_favorite_number()
                    break
            break
        elif number != 'Yes' and ~number.isdigit():
            number = input('请输入正确的数字或‘Yes’：')
        else:
            break


def print_favorite_number():
    """
    输出最喜欢的数字
    """
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print(f'你最喜欢的数字是 {favorite_number} ')
        check_number()


print_favorite_number()
