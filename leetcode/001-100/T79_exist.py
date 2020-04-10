from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        memory = [[False] * n for _ in range(m)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def dfs(i, j, memory, index):
            if index + 1 == len(word):
                return board[i][j] == word[index]
            if board[i][j] == word[index]:
                memory[i][j] = True
                for k in range(4):
                    a, b = i + dx[k], j + dy[k]
                    if 0 <= a < m and 0 <= b < n and not memory[a][b] and dfs(a, b, memory, index+1):
                        return True
                memory[i][j] = False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, memory, 0):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    words = [
        'ABCCED',
        'SEE',
        'ABCB'
    ]
    for word in words:
        print(sol.exist(board, word))