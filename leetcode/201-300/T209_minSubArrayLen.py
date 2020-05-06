class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """滑动窗口"""
        n = len(nums)
        ans = float('inf')
        left, total = 0, 0
        for i in range(n):
            total += nums[i]
            while total >= s:
                ans = min(ans, i + 1 - left)
                total -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0