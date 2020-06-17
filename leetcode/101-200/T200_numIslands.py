from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def dfs(x, y):
            grid[x][y] = '0'

            for i in range(4):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < m and 0 <= b < n and grid[a][b] == '1':
                    dfs(a, b)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans

# 方法二 并查集
class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def get_count(self):
        return self.count

    def find(self, p):
        # 寻找结点的最祖先
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # 路径压缩
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1
        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def get_index(x, y):
            return x * n + y

        # 只向下和向右扩展陆地
        dx = [1, 0]
        dy = [0, 1]
        dummy_node = m * n  # 用于连接水域的虚拟结点

        uf = UnionFind(dummy_node + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                else:
                    for k in range(2):
                        a, b = i + dx[k], j + dy[k]
                        if a < m and b < n and grid[a][b] == '1':
                            uf.union(get_index(a, b), get_index(i, j))
        return uf.get_count() - 1
