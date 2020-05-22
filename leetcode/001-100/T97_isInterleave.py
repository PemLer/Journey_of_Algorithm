class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if j == 0 and i == 0:
                    dp[i][j] = True
                elif j == 0:
                    dp[i][j] = s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]
                elif i == 0:
                    dp[i][j] = s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]
                else:
                    dp[i][j] = s3[i + j - 1] == s1[i - 1] and dp[i - 1][j] or s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    s1 = "aa"
    s2 = "ab"
    s3 = "abaa"
    print(sol.isInterleave(s1, s2, s3))
