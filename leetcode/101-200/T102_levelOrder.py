# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, depth):
        if not root:
            return
        if len(self.res) < depth+1:
            self.res.append([])
        self.res[depth].append(root.val)
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)
        
