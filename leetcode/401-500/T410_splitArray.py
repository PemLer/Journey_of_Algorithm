from typing import List


# 动态规划 O(m*n*n)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        dp[i][j] nums[0...i] 分成 j 份时最小的最大值
        """
        n = len(nums)
        pre_sum = [0] * n
        pre_sum[0] = nums[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]

        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], pre_sum[i] - pre_sum[k]))
        return dp[n][m]


# 二分 O(n*log(sum(nums)))
class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        def possible(guess):
            """判断guess为答案时需要分成多少组"""
            total = 0
            count = 1
            for i in range(n):
                if total + nums[i] > guess:
                    count += 1
                    total = nums[i]
                else:
                    total += nums[i]
            return count <= m

        # 获取二分寻找子数组和答案的二分左右起始边界
        l, r = 0, 0
        for i in range(n):
            r += nums[i]
            if l < nums[i]:
                l = nums[i]

        # 二分寻找最合适的子数组和
        while l < r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1

        return l
