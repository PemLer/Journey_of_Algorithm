class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, sub):
        if not nums:
            if sub not in self.res:
                self.res.append(sub)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], sub+[nums[i]])
        
