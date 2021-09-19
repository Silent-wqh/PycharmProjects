def quickly_model(a, b, mod):
    """快速幂取模"""
    ans = 1
    base = a % mod
    while b:
        if b & 1:
            ans = (ans * base) % mod
        base = (base * base) % mod
        b //= 2

    return ans

try:
    n = input().strip()
    n = int(n)
except EOFError:
    pass
else:
    print(quickly_model(2, n-1, 998244353))