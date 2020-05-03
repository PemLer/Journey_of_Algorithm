class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        memo = [[False] * n for _ in range(m)]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        def dfs(i, j, index):
            if index == len(word):
                return True

            for k in range(4):
                a, b = i + dx[k], j + dy[k]
                if 0 <= a < m and 0 <= b < n and not memo[a][b] and board[a][b] == word[index]:
                    memo[a][b] = True
                    if dfs(a, b, index+1):
                        return True
                    memo[a][b] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    memo[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    memo[i][j] = False
        return False