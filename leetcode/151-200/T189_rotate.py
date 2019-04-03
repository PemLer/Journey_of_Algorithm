class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0 or l == 1:
            pass
        else:
            k = k % l
            nums[:] = nums[l-k:] + nums[:l-k]
        
        
