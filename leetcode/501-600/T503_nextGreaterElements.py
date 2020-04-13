from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [0] * len(nums)

        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and nums[i%len(nums)] >= stack[-1]:
                stack.pop()
            res[i % len(nums)] = stack[-1] if stack else -1
            stack.append(nums[i])

        return res

