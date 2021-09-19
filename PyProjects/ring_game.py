total_point = int(input().strip())
init_point = int(input().strip())
mani_num = int(input().strip())
curr_point = init_point

while mani_num:
    mani = input().strip().split()
    a = int(mani[0])
    b = int(mani[1])

    mani_num -= 1
    if a:
        if (curr_point + b) > total_point:
            curr_point = b - (total_point - curr_point)
        else:
            curr_point = curr_point + b
    else:
        if (curr_point - b) < 1:
            curr_point = total_point - (b - curr_point)
        else:
            curr_point = curr_point - b

print(curr_point)
