from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]]
        """
        dp = [[0] * 2001 for _ in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            for sum in range(-1000, 1001):
                if dp[i - 1][sum + 1000] > 0:
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000]
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000]
        return 0 if S > 1000 else dp[len(nums) - 1][S + 1000]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(sol.findTargetSumWays(nums, S))
