class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        adjancy = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegree[cur] += 1
            adjancy[pre].append(cur)

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            pre = queue.pop(0)
            res.append(pre)

            for cur in adjancy[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    queue.append(cur)

        if len(res) == numCourses:
            return res
        else:
            return []