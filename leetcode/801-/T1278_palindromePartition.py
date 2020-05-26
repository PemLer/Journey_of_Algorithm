class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        dp[i][j] 到s[i]分割j次修改的最小字符数
        dp[i][j] = min(dp[i][j], dp[i0][j-1] + cost(i0, i))
        """
        def cost(i, j):
            res = 0
            while i < j:
                res += (0 if s[i] == s[j] else 1)
                i += 1
                j -= 1
            return res

        n = len(s)
        dp = [[1000] * (k + 1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    dp[i][1] = cost(0, i-1)
                else:
                    for i0 in range(j-1, i):
                        dp[i][j] = min(dp[i][j], dp[i0][j-1] + cost(i0, i-1))
        return dp[-1][-1]