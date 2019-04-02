class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(sorted(nums), [])
        return self.res
    
    def dfs(self, nums, sub):
        if sub not in self.res:
            self.res.append(sub)
        if not nums:
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], sub+[nums[i]])
