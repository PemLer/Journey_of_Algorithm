from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """
        遍历每个位置
        """
        n = len(grid)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ans += 2
                    for k in range(4):
                        a, b = i + dx[k], j + dy[k]
                        if 0 <= a < n and 0 <= b < n:
                            tmp = grid[a][b]
                        else:
                            tmp = 0
                        ans += max(0, grid[i][j] - tmp)

        return ans