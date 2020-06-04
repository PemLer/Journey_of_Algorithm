class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        dp[n] = (1 / w) * (dp[n+1] + dp[n+2] + ... + dp[n+W])
        """
        dp = [0.] * (K + W)
        s = 0
        for i in range(K, K + W):
            dp[i] = 1. if i <= N else 0.
            s += dp[i]
        for i in range(K-1, -1, -1):
            dp[i] = (1 / W) * s
            s = s - dp[i+W] + dp[i]
        return dp[0]