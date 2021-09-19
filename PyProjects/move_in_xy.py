init_point = input().strip().split()
x = int(init_point[0])
y = int(init_point[1])

curr_point = init_point

mani_num = int(input().strip())


while mani_num:
    mani = input().strip().split()
    mani_a = int(mani[0])
    mani_b = int(mani[1])

    mani_num -= 1
    if mani_a == 0:
        y += mani_b

    if mani_a == 1:
        x += mani_b

    if mani_a == 2:
        y -= mani_b

    if mani_a == 3:
        x -= mani_b

print(f'{x} {y}')
