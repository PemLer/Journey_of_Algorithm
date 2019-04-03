class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        nums = [x for x in range(1, 10)]
        self.dfs(nums, k, n, [])
        return self.res
    
    def dfs(self, nums, k, n, sub):
        if k == 0 and sum(sub) == n:
            self.res.append(sub)
            return
        elif k <= 0 or sum(sub) > n:
            return
        
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n, sub+[nums[i]])
