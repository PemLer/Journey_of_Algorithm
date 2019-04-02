class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        l = len(matrix)
        r = len(matrix[0])
        for i in range(0,l):
            for j in range(0,r):
                if matrix[i][j] == target:
                    return True
        return False
