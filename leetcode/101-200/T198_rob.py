class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <=3:
            if m == 0:
                return 0
            if m == 1:
                return nums[0]
            if m == 2:
                return max(nums[0],nums[1])
            if m == 3:
                return max(nums[1],nums[0]+nums[2])
        dp = [0] * m
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        for i in range(3,m):
            dp[i] = max(dp[i-2]+nums[i],dp[i-3]+nums[i])
        return max(dp[m-1],dp[m-2])

