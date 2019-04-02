class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                print(1)
                nums.remove(nums[i])
        return len(nums)

