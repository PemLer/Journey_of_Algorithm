from typing import List
import time
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
            if left + 1 == right:
                return 0

            return max(
                [nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left + 1, right)])

        return dp(0, len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    start_time = time.time()
    nums = [4, 1, 4, 9, 4, 1, 8, 1, 8, 6, 9, 1, 2, 0, 9, 6, 4, 1, 7, 9, 5, 4, 4, 0]
    print(sol.maxCoins(nums))
    print('cost:', time.time() - start_time)
