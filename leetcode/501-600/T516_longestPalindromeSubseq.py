from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        s[i] != s[j] dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        s[i] == s[j] dp[i][j] = dp[i+1][j-1] + 2
        dp[i][i] = 1
        dp[i-1][i] = 2 if s[i-1] == s[i]
        """

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 1
            elif i + 1 == j and s[i] == s[j]:
                return 2

            if s[i] != s[j]:
                return max(dp(i, j-1), dp(i+1, j))
            else:
                return dp(i+1, j-1) + 2

        return dp(0, len(s)-1)