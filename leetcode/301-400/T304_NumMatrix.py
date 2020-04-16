from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = self.cal_pre_sum(matrix)

    def cal_pre_sum(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])

        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        pre_sum[1][1] = matrix[0][0]

        for i in range(2, n+1):
            pre_sum[1][i] = pre_sum[1][i - 1] + matrix[0][i-1]

        for j in range(2, m+1):
            pre_sum[j][1] = pre_sum[j - 1][1] + matrix[j-1][0]

        for i in range(2, m+1):
            for j in range(2, n+1):
                pre_sum[i][j] = matrix[i-1][j-1] + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]
        return pre_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

    sol = NumMatrix(matrix)
    print(sol.sumRegion(2, 1, 4, 3))
