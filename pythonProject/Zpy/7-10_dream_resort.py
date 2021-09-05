active = True
places = []
while active:
    place = input('如果你可以到世界上任何一个地方旅游，你将会去哪？')
    if place != 'quit':
        places.append(place)
    else:
        active = False

for place in places:
    print(place, end='  ')
