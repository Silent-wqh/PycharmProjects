person_0 = {'first_name': 'Steve',
            'last_name': 'Jobs',
            'age': 22,
            'city': 'San Francisco'}
person_1 = {'first_name': 'Irvin',
            'last_name': 'Yalom',
            'age': 90,
            'city': 'Washington'}
person_2 = {'first_name': '泽东',
            'last_name': '毛',
            'age': 83,
            'city': 'Hunan'}

people = [person_0, person_1, person_2]

for pp in people:
    for key, value in pp.items():
        print(f'{key}   {value}')