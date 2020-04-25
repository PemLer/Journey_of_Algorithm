from typing import List
import collections


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node, c):
            if node in color:
                return color[node] == c

            color[node] = c

            for nei in graph[node]:
                if not dfs(nei, c ^ 1):
                    return False
            return True

        color = {}
        for node in range(1, N + 1):
            if node not in color and not dfs(node, 0):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    N = 3
    dislikes = [[1, 2], [1, 3], [2, 3]]
    print(sol.possibleBipartition(N, dislikes))
