# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False

        def is_same(a, b):
            if not a and not b:
                return True
            elif not a or not b or a.val != b.val:
                return False

            return is_same(a.left, b.left) and is_same(a.right, b.right)

        if s.val == t.val and is_same(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)