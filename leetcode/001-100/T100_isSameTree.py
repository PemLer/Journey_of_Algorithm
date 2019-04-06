# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            print(1)
            return True
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            print(2)
            return l and r
        else:
            print(3)
            return False

