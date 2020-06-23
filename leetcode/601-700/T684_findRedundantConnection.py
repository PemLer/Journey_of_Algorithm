class UnionFind:
    def __init__(self, n):
        self.par = [x for x in range(n)]

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def same(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        res = None
        for s, e in edges:
            if uf.same(s, e):
                res = [s, e]
            else:
                uf.union(s, e)
        return res