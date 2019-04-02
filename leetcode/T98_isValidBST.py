# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.T = True
        self.helper(root, res)
        return self.T

    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            if res and root.val <= res[-1]:
                self.T = False
            res.append(root.val)
            self.helper(root.right,res)

        
