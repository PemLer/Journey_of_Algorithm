class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        res = 0
        for i in nums:
            if i == 0:
                t = 0
            elif i == 1:
                t += 1
            res = max(res,t)
            
        return res
