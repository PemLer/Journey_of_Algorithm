class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        l = 0
        r = le - 1
        a = sorted(nums)
        while a[l] == nums[l] and l < r:
            l += 1
        while a[r] == nums[r] and l < r:
            r -= 1
        if l == r:
            return 0
        else:
            return r - l + 1


