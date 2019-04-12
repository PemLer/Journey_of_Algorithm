class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == len(list(set(nums))):
            return 1
        if len(nums) == 1:
            return 1
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = 0
        li = []
        for key in d:
            if d[key] > m:
                m = d[key]
                li = []
                li = [key]
            elif d[key] == m:
                li.append(key)

        l = len(li)
        res = 50000
        for i in range(0,l):
            left = 0
            right = len(nums) -1
            while nums[left] != li[i] or nums[right] != li[i]:
                if nums[left] != li[i]:
                    left += 1
                if nums[right] != li[i]:
                    right -= 1
            res = min(res,right-left+1)
        return res

