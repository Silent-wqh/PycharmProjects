my_pies = ['麻辣鸡肉', '香辣鱿鱼', '酱香肉']
friend_pies = my_pies[:]
my_pies.append('鸡腿')
friend_pies.append('茄子')
print('My favorite pies are:')
for my_pie in my_pies:
    print(my_pie)
print('Friends favorite pies are:')
for friend_pie in friend_pies:
    print(friend_pie)