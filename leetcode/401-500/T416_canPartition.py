from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total >> 1
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j and dp[i - 1][j - nums[i - 1]] or nums[i-1] == j or dp[i-1][j]:
                    dp[i][j] = True
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 5]
    print(sol.canPartition(nums))
