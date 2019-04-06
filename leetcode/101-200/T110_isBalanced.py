# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        self.helper(root)
        return self.flag
        
    def helper(self, root):
        if not root or self.flag == False:
            return 0
        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1
        if abs(left-right) > 1:
            self.flag = False
        return max(left, right)
