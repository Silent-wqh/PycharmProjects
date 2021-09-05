favorite_places = {'Amy': ['山东临沂', '山东菏泽曹县'],
                   'Bob': ['河南郑州', '湖北武汉'],
                   'Cindy': ['广东深圳', '四川成都']}

for name, places in favorite_places.items():
    print(f'{name}', end='  ')
    for place in places:
        print(place, end='  ')
    print()
