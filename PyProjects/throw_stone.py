
try:
    n = input().strip()
    n = int(n)
except EOFError:
    pass
else:
    print((2**n)%998244353)