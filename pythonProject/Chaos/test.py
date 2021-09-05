def count_words(filename):
    """
    计算展示单词数和展示最高频率前10的单词
    :param filename: 文件名，包含路径
    """
    from collections import Counter

    words = []
    try:
        with open(filename, encoding='utf-8') as file_object:
            words = file_object.read().split()
    except FileNotFoundError:
        print('文件未找到')
    else:
        print(len(words))
        print(Counter(words).most_common(10))


count_words('../Zpy/Pride and Prejudice.txt')