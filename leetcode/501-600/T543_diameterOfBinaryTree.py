# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self. helper(root.right)
        self.res = max(self.res, left+right)
        return max(left, right) + 1
