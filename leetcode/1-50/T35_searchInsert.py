class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
                elif i != 0 and nums[i] > target and nums[i-1] < target:
                    return i

