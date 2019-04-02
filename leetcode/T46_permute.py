class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, sub):
        if not nums:
            self.res.append(sub)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], sub+[nums[i]])
        
