# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def v(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, sub):
        if not root:
            return
        if not root.left and not root.right:
            self.res += sub*10+root.val
            return
        self.dfs(root.left, sub*10+root.val)
        self.dfs(root.right, sub*10+root.val)
            
        
