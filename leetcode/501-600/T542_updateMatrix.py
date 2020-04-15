from typing import List

# 方法一 动态规划
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dp = [[10 ** 9] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0

        # left up
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        # left down
        for i in range(m-1, -1, -1):
            for j in range(n):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        # right up
        for i in range(m):
            for j in range(n-1, -1, -1):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

        # right down
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

        return dp


# 方法二 DFS
import collections
class Solution2:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        zeros = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        q = collections.deque(zeros)
        seen = set(zeros)

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while q:
            x, y = q.popleft()
            for i in range(4):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < m and 0 <= b < n and (a, b) not in seen:
                    dp[a][b] = dp[x][y] + 1
                    seen.add((a, b))
                    q.append((a, b))

        return dp



if __name__ == '__main__':
    sol = Solution2()
