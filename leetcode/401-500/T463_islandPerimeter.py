class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        t = 0
        l = len(grid)
        r = len(grid[0])
        for i in range(0,l):
            for j in range(0,r):
                if grid[i][j] == 1:
                    count += 1
                    if j+1 < r and grid[i][j] == grid[i][j+1]:
                        t += 1
                    if i+1 < l and grid[i][j] == grid[i+1][j]:
                        t += 1
        return 4*count-2*t
        
