class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.dfs(1,n,k,sub)
        return self.res
    
    def dfs(self,i,n,k,sub):
        if k == 0:
            self.res.append(sub)
            return
        for i in range(i,n+1):
            self.dfs(i+1,n,k-1,sub+[i])
