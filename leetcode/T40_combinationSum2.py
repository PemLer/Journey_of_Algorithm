class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(sorted(candidates), target, [])
        return self.res
    
    def dfs(self, candidates, target, sub):
        if sum(sub) == target and sub not in self.res:
            self.res.append(sub)
            return
        if sum(sub) > target:
            return
        
        for i in range(len(candidates)):
            self.dfs(candidates[i+1:], target, sub+[candidates[i]])
