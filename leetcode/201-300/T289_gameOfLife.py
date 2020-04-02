class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        定义复合状态，记录变化前后
        -1 活 --> 死
        2 死 --> 活
        """
        m, n = len(board), len(board[0])
        dx = [-1, 0, 1, 1, 1, 0, -1, -1]
        dy = [1, 1, 1, 0, -1, -1, -1, 0]

        def calc(x, y):
            """
            计算(x, y)周围八个位置的活细胞个数
            """
            count = 0
            for i in range(8):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < m and 0 <= b < n:
                    if board[a][b] == 1 or board[a][b] == -1:
                        count += 1
            return count

        for i in range(m):
            for j in range(n):
                count = calc(i, j) 
                # rule 1
                if board[i][j] == 1 and count < 2:
                    board[i][j] = -1
                # rule 2
                elif board[i][j] == 1 and 2 <= count <= 3:
                    pass
                # rule 3
                elif board[i][j] == 1 and count > 3:
                    board[i][j] = -1
                # rule 4
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
