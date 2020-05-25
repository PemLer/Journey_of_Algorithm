class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        s[i] == t[j]
          dp[i][j] = dp[i-1][j-1]
        otherwise
          dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(0, m+1):
            for j in range(0, n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]