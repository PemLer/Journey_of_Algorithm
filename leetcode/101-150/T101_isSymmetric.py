# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            l = self.helper(p.left, q.right)
            r = self.helper(p.right, q.left)
            return l and r
        else:
            return False
        
