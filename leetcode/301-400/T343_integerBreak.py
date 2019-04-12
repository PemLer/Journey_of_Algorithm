class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        dp = [1] * (n+1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j] * dp[j])
        # print(dp[-1])
        return dp[-1]
