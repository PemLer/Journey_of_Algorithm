class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [[nums[i]] for i in range(n)]
        ans = 1
        res = [nums[0]]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
                    if len(dp[i]) > ans:
                        ans = len(dp[i])
                        res = dp[i]
        return res
