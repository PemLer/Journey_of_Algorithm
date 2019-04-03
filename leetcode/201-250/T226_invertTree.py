# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        temp = TreeNode(0)
        if root is None:
            return
        if root:
            temp.left = root.left
            root.left = root.right
            root.right = temp.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root

