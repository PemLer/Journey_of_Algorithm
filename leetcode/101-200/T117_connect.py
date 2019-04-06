"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        first = root
        while root:
            dummy = Node(0, None, None, None)
            tail = dummy
            while root:
                if root.left:
                    tail.next = root.left
                    tail = tail.next
                if root.right:
                    tail.next = root.right
                    tail = tail.next
                root = root.next
            tail.next = None
            root = dummy.next
        return first
