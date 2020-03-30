def solve():
    s = input()
    a, b, p = map(int, s.split(' '))

    res = 1 % p
    while b:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1

    return res

print(solve())
