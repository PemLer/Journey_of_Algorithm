from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        units = [set() for _ in range(n)]

        for i in range(n * n):
            row = i // n
            col = i % n
            unit = 3 * (row // 3) + col // 3

            value = board[row][col]
            if value != '.':
                if value not in rows[row] and value not in cols[col] and value not in units[unit]:
                    rows[row].add(value)
                    cols[col].add(value)
                    units[unit].add(value)
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    a = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(sol.isValidSudoku(a))
