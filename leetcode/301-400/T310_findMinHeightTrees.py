from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        map = collections.defaultdict(set)
        for a, b in edges:
            map[a].add(b)
            map[b].add(a)

        queue = [k for k, v in map.items() if len(v) == 1]
        while n > 2:
            tmp = []
            for q in queue:
                t = map[q].pop()
                map[t] -= {q}
                if len(map[t]) == 1:
                    tmp.append(t)
                n -= 1
            queue = tmp

        return queue


if __name__ == '__main__':
    sol = Solution()
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(sol.findMinHeightTrees(n, edges))
