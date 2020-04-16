from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    target = 4
    print(sol.combinationSum4(nums, target))
