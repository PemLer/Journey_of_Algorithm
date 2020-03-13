"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        def add_node(lst, node):
            if node:
                lst.append(node)

        curr_layer = [root]
        next_layer = []
        while curr_layer:
            for i in range(len(curr_layer) - 1):
                curr_layer[i].next = curr_layer[i+1]
                add_node(next_layer, curr_layer[i].left)
                add_node(next_layer, curr_layer[i].right)
            curr_layer[-1].next = None
            add_node(next_layer, curr_layer[-1].left)
            add_node(next_layer, curr_layer[-1].right)
            curr_layer = next_layer[:]
            next_layer = []
        return root

                

