i = 0 # 总金币数
k = int(input().strip()) # 总天数
m = 1 # 可获得金币数
n = 1 # 当天金币数获得天数
for ks in range(1, k+1):
    if n == m:
        i += m
        m += 1
        n = 1
    else:
        n += 1
        i += m

print(i)

# 1 2 2 3 3 3

