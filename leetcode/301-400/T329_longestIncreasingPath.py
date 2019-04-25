class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        def dp(x, y):
            if f[x][y] != -1:
                return f[x][y]
            f[x][y] = 1
            for i in range(4):
                a, b = x+dx[i], y+dy[i]
                if a >= 0 and a < n and b >= 0 and b < m and g[a][b] < g[x][y]:
                    f[x][y] = max(f[x][y], dp(a, b) + 1)
            return f[x][y]
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        g = matrix
        n, m = len(g), len(g[0])
        f = [[-1 for i in range(m)] for j in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dp(i, j))
        
        return res
