class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in nums:
            #assert(i >= 0 and i <= 2)
            count[i] += 1

        index = 0
        for i, num in enumerate(count):
            for j in range(num):
                nums[index] = i
                index += 1
