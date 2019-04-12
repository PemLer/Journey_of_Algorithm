class Solution(object):
    def makesquare(self, nums):
        length = sum(nums)
        if length % 4 != 0 or len(nums) < 4:
            return False
        side = length // 4
        bucket = [0, 0, 0, 0]
        nums.sort(reverse=True)
        return self.dfs(nums, side, bucket, 0)
        
    def dfs(self, nums, side, bucket, i):
        if i == len(nums):
            if bucket[0] == bucket[1] == bucket[2] == bucket[3] == side:
                return True
            else:
                return False
        for k in range(4):
            if nums[i] + bucket[k] <= side:
                bucket[k] += nums[i]
                if self.dfs(nums, side, bucket, i+1):
                    return True
                bucket[k] -= nums[i]
        return False
        
