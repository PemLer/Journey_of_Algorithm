from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_sum = [1] * (n + 1)
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] * num
        product = 1
        res = [0] * n
        for i in range(n-1, -1, -1):
            res[i] = pre_sum[i] * product
            product *= nums[i]
        return res