"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = [root]
        res = 1
        while queue:
            tmp = []
            for q in queue:
                if q.children:
                    for node in q.children:
                        tmp.append(node)
            if tmp:
                res += 1
            queue = tmp[:]
        return res