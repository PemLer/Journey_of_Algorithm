# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, depth):
        if not root:
            self.res = max(self.res, depth)
            return 
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)
