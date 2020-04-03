from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        freshs = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshs[(i, j)] = 0
        if not queue and not freshs:
            return 0
        if not queue and freshs:
            return -1

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                    grid[a][b] = grid[x][y] + 1
                    freshs.pop((a, b))
                    queue.append((a, b))

        if freshs:
            return -1
        else:
            return grid[x][y] - 2


if __name__ == '__main__':
    sol = Solution()
    grids = [
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
        [[0]],
        [[1]]
    ]
    for grid in grids:
        print(sol.orangesRotting(grid))
