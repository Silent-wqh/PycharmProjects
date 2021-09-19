import math
try:
    num = int(input().strip())
except EOFError:
    pass
else:
    max_ff = 0 # 最大整数
    for i in range(2 , int(math.sqrt(num))+1):
        if (num / i) == (num // i):
            print(num // i)
            break

