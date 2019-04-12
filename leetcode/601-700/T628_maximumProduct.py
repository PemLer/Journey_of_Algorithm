class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res_left = nums[0:2] + [nums[-1]]
        res_right = nums[-3:]
        left = res_left[0]*res_left[1]*res_left[2]
        right = res_right[0]*res_right[1]*res_right[2]
        return max(left,right)
        
        
