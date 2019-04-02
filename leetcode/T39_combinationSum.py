class Solution:
    def combinationSum(self, candidates, target: int):
        self.res = []
        self.dfs(candidates, target, [])
        return self.res
    
    def dfs(self, candidates, target, sub):
        if sum(sub) == target:
            self.res.append(sub)
            return 
        if sum(sub) > target:
            return
        
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target, sub+[candidates[i]])
