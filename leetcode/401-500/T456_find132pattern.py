from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_stack = [0] * n
        min_stack[0] = nums[0]
        for i in range(1, n):
            min_stack[i] = min(min_stack[i-1], nums[i])

        stack = []
        for i in range(n-1, 0, -1):
            if nums[i] > min_stack[i]:
                while stack and stack[-1] <= min_stack[i]:
                    stack.pop()
                if stack and nums[i] > stack[-1]:
                    return True
                stack.append(nums[i])

        return False