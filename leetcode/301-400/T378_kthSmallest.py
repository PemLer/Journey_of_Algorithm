class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def check(target):
            i, j = m - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        i, j = matrix[0][0], matrix[m - 1][n - 1]
        while i < j:
            mid = i + j >> 1
            if check(mid):
                j = mid
            else:
                i = mid + 1
        return i