class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        r = len(matrix[0])
        d = {}
        for i in range(0,l):
            for j in range(0,r):
                if matrix[i][j] == 0:
                    d[(i,j)] = 0

        for key in d:
            matrix[key[0]] = [0] * r
            for x in matrix:
                x[key[1]] = 0

