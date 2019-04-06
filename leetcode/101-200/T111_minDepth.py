# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.m = 0
        i = 0
        self.helper(root,i)
        return self.m
    
    def helper(self,root,i):
        if not root: return
        else:
            i += 1
            if not root.left and not root.right:
                if self.m == 0 or self.m == 1: self.m = i
                else: self.m = min(self.m,i)
                return
            self.helper(root.left,i)
            self.helper(root.right,i)
        
        
