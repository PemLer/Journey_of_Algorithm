from typing import List
import time
from functools import lru_cache


# 方法一 记忆化存储+递归
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        假设最后戳破的是i
        """
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
            if left + 1 == right:
                return 0

            return max(
                [nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left + 1, right)])

        return dp(0, len(nums) - 1)


# 方法二 递推
class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        """
        假设最后戳破的是i
        """
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][-1]


if __name__ == '__main__':
    sol = Solution()
    start_time = time.time()
    nums = [4, 1, 4, 9, 4, 1, 8, 1, 8, 6, 9, 1, 2, 0, 9, 6, 4, 1, 7, 9, 5, 4, 4, 0]
    print(sol.maxCoins(nums))
    print('cost:', time.time() - start_time)
