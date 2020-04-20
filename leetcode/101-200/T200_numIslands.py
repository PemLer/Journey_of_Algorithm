from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def dfs(x, y):
            grid[x][y] = '0'

            for i in range(4):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < m and 0 <= b < n and grid[a][b] == '1':
                    dfs(a, b)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans