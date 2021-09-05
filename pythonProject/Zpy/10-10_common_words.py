def count_words(filename, word):
    """
    计算文本中某个单词的出现次数
    :param filename: 文件名，包含路径
    :param word: 要查找的单词
    """
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents.lower().count(word))

while(1):
    word = input('输入你想查询的单词：')
    if word == '__quit__':
        break
    try:
        count_words('Pride and Prejudice.txt', word)
    except FileNotFoundError:
        print('文件未找到')