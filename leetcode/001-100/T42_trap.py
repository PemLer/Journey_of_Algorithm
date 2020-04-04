from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        动态规划，左右最高
        """
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(1, n):
            max_left[i] = max(height[i - 1], max_left[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        ans = 0
        for i in range(1, n - 1):
            h = min(max_left[i], max_right[i])
            if h > height[i]:
                ans += h - height[i]

        return ans