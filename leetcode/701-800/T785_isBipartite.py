class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A = set()
        B = set()
        record = set()
        n = len(graph)
        queue = []

        i = 0
        while len(record) < n:
            while queue:
                node = queue.pop(0)
                if node in A:
                    t = B
                    o = A
                else:
                    t = A
                    o = B
                for next_node in graph[node]:
                    if next_node not in record:
                        queue.append(next_node)
                        t.add(next_node)
                        record.add(next_node)
                    elif next_node in o:
                        return False

            while i < n:
                if i not in record and graph[i]:
                    A.add(i)
                    record.add(i)
                    queue = [i]
                    break
                else:
                    record.add(i)
                    i += 1

        return True
