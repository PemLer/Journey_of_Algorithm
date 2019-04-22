class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for i in range(col)] for j in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                res = max(dp[i][j], res)
        return res ** 2
