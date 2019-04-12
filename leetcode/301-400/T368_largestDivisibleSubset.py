class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        nums.sort()
        dp = [0] * n
        dp1 = [[]] * n
        dp[0] = 1
        dp1[0] = [nums[0]]
        tmp = 1
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] % nums[j] == 0:
                    dp[i] = dp[j] + 1
                    if dp[i] >= tmp:
                        tmp = dp[i]
                        dp1[i] = dp1[j]+[nums[i]]
                    # else:
                    #     dp1[i] = [nums[i]]
                elif not dp[i]:
                    dp[i] = 1
                    dp1[i] = [nums[i]]
        # print(dp)
        # print(dp1)
        for i in dp1:
            if len(i) == tmp:
                return i
