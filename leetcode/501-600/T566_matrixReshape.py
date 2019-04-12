class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        tmp = []
        if m*n != r*c:
            return nums
        for i in range(m):
            for j in range(n):
                tmp.append(nums[i][j])
        
        res = [[0]*c for i in range(r)]
        t = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[t]
                t += 1
                
        return res
        
