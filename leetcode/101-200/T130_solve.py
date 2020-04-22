from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        def dfs(i, j):

            for k in range(4):
                a, b = i + dx[k], j + dy[k]
                if 0 <= a < m and 0 <= b < n and board[a][b] == 'O':
                    board[a][b] = '#'
                    dfs(a, b)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == 'O':
                    board[i][j] = '#'
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        print(board)


if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol = Solution()
    sol.solve(board)