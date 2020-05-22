class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """先找出最长公共子序列，然后去拼找结果"""
        n, m = len(str1), len(str2)
        dp = [['' for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
        lcm = dp[-1][-1]
        i, j = 0, 0
        res = ''
        for char in lcm:
            while i < n and str1[i] != char:
                res += str1[i]
                i += 1
            while j < m and str2[j] != char:
                res += str2[j]
                j += 1
            res += char
            i += 1
            j += 1

        res += str1[i:]
        res += str2[j:]
        return res