class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(1,i):
                if i%j == 0:
                    dp[i] = min(dp[i],dp[j]+i//j)
        return dp[-1]
