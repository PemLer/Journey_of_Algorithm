# DP O(d*n*n)

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        dp[i][j] = min(dp[i][j], dp[i0][j-1] + cal_max(i0, i))
        """
        n = len(jobDifficulty)
        if d > n:
            return -1
        elif d == n:
            return sum(jobDifficulty)
        dp = [[300001] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(i, d) + 1):
                for k in range(j, i+1):
                    dp[i][j] = min(dp[i][j], dp[k-1][j-1] + max(jobDifficulty[k-1:i]))
        return dp[-1][-1]
