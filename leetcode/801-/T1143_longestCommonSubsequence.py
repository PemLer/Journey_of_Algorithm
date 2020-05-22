class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1 t1[i] == t2[j]
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        2 otherwise
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
        """
        n, m = len(text1), len(text2)
        if n == 0 or m == 0:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]