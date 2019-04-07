class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        up, right = 0, col-1
        while up < row and right > -1:
            if matrix[up][right] == target:
                return True
            elif matrix[up][right] < target:
                up += 1
            else:
                right -= 1
        return False
        
