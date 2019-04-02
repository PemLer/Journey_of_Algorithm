class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0,n):
            for j in range(0,i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        i = 0
        j = n-1
        while i < j:
            for k in range(0,n):
                matrix[k][i],matrix[k][j] = matrix[k][j],matrix[k][i]
            i += 1; j -= 1

