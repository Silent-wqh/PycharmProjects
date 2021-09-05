loving_nums = {'Amy': [8, 5],
               'Bob': [9, 6],
               'Cindy': [4, 3],
               'David': [5, 2],
               'Einstein': [7, 1]
               }

for name, numbers in loving_nums.items():
    print(name, end='  ')
    for number in numbers:
        print(number, end='  ')
    print()