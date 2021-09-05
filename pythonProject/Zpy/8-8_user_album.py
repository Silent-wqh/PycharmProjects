def make_album(singer, album, quantity = ''):
    """存储信息，返回字典"""
    if quantity:
        return {'singer': singer, 'album': album, 'quantity': quantity}
    else:
        return {'singer': singer, 'album': album}

album_lists = []

while True:
    singer = input('请输入歌手名：')
    if singer == 'quit':
        break
    album = input('请输入专辑：')
    quantity = input('请输入数量：')
    album_lists.append(make_album(singer, album, quantity))


for album_list in album_lists:
    for key, value in album_list.items():
        print(f'{key}: {value}', end='  ')
    print()

