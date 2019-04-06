class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in range(0,len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[t+1] = nums[i+1]
                t += 1
        del nums[t+1:]
        return len(nums)

