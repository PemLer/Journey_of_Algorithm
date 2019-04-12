class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return  1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
            return 0

        ares = [dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]]
        if ares:
            return max(ares)
        return 0

