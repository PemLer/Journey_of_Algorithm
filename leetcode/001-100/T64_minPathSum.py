class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(0,m)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])

        return dp[m-1][n-1]
