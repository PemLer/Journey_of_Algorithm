class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
        
    def backtrack(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.check(row, col, board) and self.backtrack(board):
                            return True
                        board[row][col] = '.'
                    return False
        return True
    
    def check(self, x, y, board):
        tmp = board[x][y]
        board[x][y] = '.'
        for val in board[x]:
            if val == tmp:
                return False
        for i in range(9):
            if tmp == board[i][y]:
                return False
        for m in range(3):
            for n in range(3):
                if board[(x//3)*3+m][(y//3)*3+n] == tmp:
                    return False
        board[x][y] = tmp
        return True
                        
        
