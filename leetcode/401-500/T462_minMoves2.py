class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums)//2]
        res = 0
        for i in nums:
            res += abs(i-mid)
        return res
        
