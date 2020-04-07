# 读取数据
n = int(input())
lst = [0] * (n * n)
i = 0
while i < len(lst):
    for num in map(int, input().split()):
        lst[i] = num
        i += 1

grid = [[0] * (n + 1) for _ in range(n+1)]

for i, num in enumerate(lst):
    x, y = i // n + 1, i % n + 1
    grid[x][y] += num + grid[x-1][y]


ans = float('-inf')
for i in range(1, n+1):
    for j in range(i+1, n+1):
        last = 0
        for k in range(1, n+1):
            cur = grid[j][k] - grid[i][k]
            last = max(0, last) + cur
            ans = max(ans, last)

print(ans)


