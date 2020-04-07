n = int(input())

cows = [[0] * 3 for _ in range(n)]
for i in range(n):
    w, s = map(int, input().split())
    cows[i] = [w, s, w + s]

cows.sort(key=lambda x: x[2])

total = 0
res = float('-inf')
for w, s, _ in cows:
    res = max(res, total - s)
    total += w

print(res)
