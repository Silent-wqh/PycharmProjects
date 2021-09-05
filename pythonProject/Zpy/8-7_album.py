def make_album(singer, album, quantity = ''):
    if quantity:
        return {'singer': singer, 'album': album, 'quantity': quantity}
    else:
        return {'singer': singer, 'album': album}

album_lists = []
album_lists.append(make_album('许嵩', '苏格拉没有底'))
album_lists.append(make_album('周杰伦', '魔杰座', 50))
album_lists.append(make_album('蔡依林', '特务J', 60))

for album_list in album_lists:
    for key, value in album_list.items():
        print(f'{key}: {value}', end='  ')
    print()

