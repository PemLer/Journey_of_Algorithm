class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sum(nums)
        b = sum([x for x in range(0,len(nums)+1)])
        return b-a
        
