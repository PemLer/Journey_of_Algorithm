# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.res.append(root.val)
        
