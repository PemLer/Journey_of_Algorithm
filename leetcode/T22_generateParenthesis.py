class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(n, n, n, '')
        return self.res
    
    def dfs(self, n, left, right, sub):
        if left == 0 and right == 0:
            self.res.append(sub)
            return
        
        if left > 0:
            self.dfs(n, left-1, right, sub+'(')
        if right > left:
            self.dfs(n, left, right-1, sub+')')
        
