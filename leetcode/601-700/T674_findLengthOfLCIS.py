from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans, res = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                ans += 1
                res = max(res, ans)
            else:
                ans = 1
        return res