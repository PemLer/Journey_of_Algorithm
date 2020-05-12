# 方法一 三维dp
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def stat(str):
            a, b = 0, 0
            for s in str:
                if s == '0':
                    a += 1
                else:
                    b += 1
            return a, b

        le = len(strs)

        @functools.lru_cache(None)
        def dp(i, j, k):
            if i == 0 and j == 0 or k == 0:
                return 0
            a, b = stat(strs[k - 1])

            if i >= a and j >= b:
                return max(dp(i - a, j - b, k - 1) + 1, dp(i, j, k - 1))
            else:
                return dp(i, j, k - 1)

        return dp(m, n, le)

# 方法二 二维dp
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def stat(str):
            a, b = 0, 0
            for s in str:
                if s == '0':
                    a += 1
                else:
                    b += 1
            return a, b

        for str in strs:
            a, b = stat(str)
            for i in range(m, a-1, -1):
                for j in range(n, b-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-a][j-b] + 1)
        return dp[-1][-1]
