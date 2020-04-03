class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

# DFS

class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        node_clone = Node(node.val, [])
        self.visited[node] = node_clone

        node_clone.neighbors = [self.cloneGraph(nod) for nod in node.neighbors]

        return node_clone


# BFS

from collections import deque

class Solution2:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}

        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]