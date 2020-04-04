"""
前缀和
"""

m = n = 5001
# 读取数据
N, R = map(int, input().split())

R = min(5001, R)

s = [[0] * 5010 for _ in range(5010)]

for _ in range(N):
    x, y, w = map(int, input().split())
    x += 1
    y += 1
    s[x][y] += w


def solve(grid, R):
    # 预处理前缀和
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

    ans = 0

    # 枚举所有边长为R的矩形，枚举(i, j)为右下角
    for i in range(R, m + 1):
        for j in range(R, n + 1):
            ans = max(ans, s[i][j] - s[i - R][j] - s[i][j - R] + s[i - R][j - R])

    return ans


print(solve(s, R))
