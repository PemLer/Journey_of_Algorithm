class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        d = {}
        count = 0
        t = 1
        l = len(nums)
        if k == 0:
            for i in nums:
                if i in d and d[i] < 2:
                    d[i] = 2
                    count += 1
                elif i not in d:
                    d[i] = 1
        else:
            nums = set(nums)
            for i in nums:
                if k + i in d:
                    count += 1
                if i - k in d:
                    count += 1
                d[i] = 1
        return count

