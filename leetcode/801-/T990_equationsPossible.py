class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, index):
        if index == self.parent[index]:
            return index
        self.parent[index] = self.find(self.parent[index])
        return self.find(self.parent[index])

    def union(self, index1, index2):
        self.parent[self.find(index1)] = self.find(index2)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for equ in equations:
            if equ[1] == '=':
                index1 = ord(equ[0]) - ord('a')
                index2 = ord(equ[-1]) - ord('a')
                uf.union(index1, index2)
        for equ in equations:
            if equ[1] == '!':
                index1 = ord(equ[0]) - ord('a')
                index2 = ord(equ[-1]) - ord('a')
                if uf.find(index1) == uf.find(index2):
                    return False
        return True