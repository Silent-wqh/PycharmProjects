import math


while True:
    number = int(input().strip())
    sq_number = int(math.sqrt(number))
    judge_num = 0
    for num in range(2, sq_number+1):
        a = number / num
        if a == int(a):
            judge_num += 1
    if judge_num:
        print(0)
    else:
        print(1)
