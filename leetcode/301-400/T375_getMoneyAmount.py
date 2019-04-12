class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [[0]*(n+1) for _ in range(0,n+1)]
        """ dp[][i] = i + max(dp[1][i-1]+dp[i+1][n]) """
        dp[0][0] = 0
        for low in range(n,0,-1):
            for high in range(low+1,n+1):
                dp[low][high] = min(x + max(dp[low][x-1],dp[x+1][high]) for x in range(low,high))
        return dp[1][n]


