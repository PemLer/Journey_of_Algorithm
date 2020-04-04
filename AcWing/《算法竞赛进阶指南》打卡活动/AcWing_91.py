"""

1 哪些点被用过
2 目前停在哪个点上

2^20 * 20

f[state][j] = f[state_k][k] + weight[k][j], state_k = state除掉j之后的集合，state_k要包含k

state用二进制表示集合

0，1，4

state = 10011

"""

# 读取数据
n = int(input())

# print(n)
weight = [[0] * n for _ in range(n)]

for i in range(n):
    s = list(input().split())
    # print(s)
    for j, char in enumerate(s):
        weight[i][j] = int(char)


# print(weight)

def solve(weight, n):
    m = 1 << n
    dp = [[99999] * n for _ in range(m)]
    dp[1][0] = 0
    for i in range(1 << n):
        for j in range(n):
            if i >> j & 1:
                for k in range(n):
                    if (i - (1 << j) >> k & 1):
                        dp[i][j] = min(dp[i][j], dp[i - (1 << j)][k] + weight[k][j])
    return dp[(1 << n) - 1][n - 1]


print(solve(weight, n))


