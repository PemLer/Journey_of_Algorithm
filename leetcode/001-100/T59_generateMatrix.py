from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, 0
        i = 0
        for num in range(1, n * n + 1):
            matrix[x][y] = num
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and not matrix[x + dx[i]][y + dy[i]]:
                x, y = x + dx[i], y + dy[i]
            else:
                i = (i + 1) % 4
                x, y = x + dx[i], y + dy[i]
        return matrix


if __name__ == '__main__':
    sol = Solution()
    nums = [
        1,2,3,4,5,6
    ]
    for num in nums:
        print(sol.generateMatrix(num))
