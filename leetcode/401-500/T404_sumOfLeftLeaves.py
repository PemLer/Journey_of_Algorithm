# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, tag):
        if not root:
            return
        if tag == 1 and not root.left and not root.right:
            self.res += root.val
        self.dfs(root.left, 1)
        self.dfs(root.right, 0)