# 方法一 反向思维
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])
        return n - dp[0][-1]


# 方法二 正向思维
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = dp[j + 1][i - 1]
                else:
                    dp[j][i] = min(dp[j + 1][i], dp[j][i - 1]) + 1
        return dp[0][-1]
