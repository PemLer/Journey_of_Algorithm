class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for __ in range(row)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    if r > 0:
                        dp[r][c] += dp[r-1][c]
                    if c > 0:
                        dp[r][c] += dp[r][c-1]
        return dp[row-1][col-1]
