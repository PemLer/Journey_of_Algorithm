from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        # print('indegrees:', indegrees)
        # print('adjacency:', adjacency)
        queue = deque()
        for i, t in enumerate(indegrees):
            if t == 0:
                queue.append(i)

        while queue:
            # print(queue)
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        return not numCourses


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[0,1]]
    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))