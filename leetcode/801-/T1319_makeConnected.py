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

    def normalize(self):
        for i in range(len(self.par)):
            self.find(i)

    def get_count(self):
        self.normalize()
        return len(set(self.par))


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n - 1:
            return -1
        uf = UnionFind(n)
        for s, e in connections:
            uf.union(s, e)
        return uf.get_count() - 1