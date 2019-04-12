class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        l = len(nums)
        if l == 0:
            return
        self.dp = [0]*l
        self.dp[0] = nums[0]
        if l > 0:
            for i in range(1,l):
                self.dp[i] = self.dp[i-1] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
