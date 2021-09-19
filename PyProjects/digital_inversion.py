try:
    num = input().strip()
    k = len(str(num)) - 1  # 幂
    num = int(num)
    flags = False
    if num < 0:
        num = -num
        k = len(str(num)) - 1  # 幂
        flags = True # 负数标志
except EOFError:
    exit()
else:
    o_num = 0 # 需要输出的数
    while True:
        if (num+9) // 10:
            temp = num % 10
            o_num += temp * 10**k
            k -= 1
            num  = num // 10
        else:
            break

    if flags:
        o_num = -o_num
    print(o_num)

