class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                break
            matrix = self.rotate(matrix)
        return res
    
    def rotate(self, matrix):
        new_mat = []
        row = len(matrix)
        col = len(matrix[0])
        for j in range(col):
            tmp_mat = []
            for i in range(row):
                tmp_mat.append(matrix[i][j])
            new_mat.append(tmp_mat)
        new_mat.reverse()
        return new_mat
        
