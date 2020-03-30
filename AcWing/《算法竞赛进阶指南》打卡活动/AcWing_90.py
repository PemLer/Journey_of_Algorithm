def solve():
    a = int(input())
    b = int(input())
    p = int(input())
    res = 0
    while b:
        if b & 1:
            res = (res + a) % p
        a = (a + a) % p
        b >>= 1
    return res

print(solve())
