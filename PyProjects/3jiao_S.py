import math


while True:
    a = input().strip().split(' ')
    try:
        b = (int(a[0]) + int(a[1]) + int(a[2])) / 2
        c = math.sqrt(b*(b-int(a[0]))*(b-int(a[1]))*(b-int(a[2])))
    except EOFError:
        break
    print(f'{c:.2f}')

