from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if not queue or len(queue) == n * n:
            return -1
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < n and 0 <= b < n and not grid[a][b]:
                    grid[a][b] = grid[x][y] + 1
                    queue.append((a, b))
        return grid[x][y] - 1


if __name__ == '__main__':
    sol = Solution()
    grids = [
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    ]
    for grid in grids:
        print(sol.maxDistance(grid))
