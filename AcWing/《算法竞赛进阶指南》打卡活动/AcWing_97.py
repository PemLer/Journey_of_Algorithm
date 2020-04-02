mod = 9901

def qmi(a, k):
    res = 1
    while k:
        if k & 1:
            res = res * a % mod
        a = a * a % mod
        k >>= 1
    return res


def sum(p, i):
    if i == 0:
        return 1
    elif i % 2 == 0:
        return (p % mod * sum(p, i-1) + 1) % mod  # 右移一位
    else:
        return (1 + qmi(p, i//2 + 1)) * sum(p, i//2) % mod


def solve(A, B):
    res = 1
    for i in range(2, A+1):
        s = 0
        while A % i == 0:
            s += 1
            A //= i
        if s:
            res = res * sum(i, s * B) % mod
    if not A:
        return 0
    return res

A, B = map(int, input().split())
print(solve(A, B))

