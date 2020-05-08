
# 方法一 DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n

        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)

        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1
        return count


# 方法二 BFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        queue = []
        count = 0
        visited = [0] * n

        for i in range(n):
            if visited[i] == 0:
                count += 1
                visited[i] = 1
                queue.append(i)
                while queue:
                    index = queue.pop(0)
                    for j in range(n):
                        if M[index][j] == 1 and visited[j] == 0:
                            visited[j] = 1
                            queue.append(j)
        return count