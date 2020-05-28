class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                dp[i][j] = min(k + 1 + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j))  # k+1
        return dp[0][-1]