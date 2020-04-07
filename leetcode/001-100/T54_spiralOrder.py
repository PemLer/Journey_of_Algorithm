from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        res = []
        memory = [[False] * n for _ in range(m)]
        x, y = 0, 0
        i = 0
        for _ in range(m * n):
            num = matrix[x][y]
            res.append(num)
            memory[x][y] = True
            a, b = x + dx[i], y + dy[i]
            if a < 0 or a >= m or b < 0 or b >= n or memory[a][b]:
                i = (i + 1) % 4
            x, y = x + dx[i], y + dy[i]
        return res


if __name__ == '__main__':
    sol = Solution()
    a = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    print(sol.spiralOrder(a))
