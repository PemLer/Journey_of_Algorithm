# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.sub = []
        self.helper(root, 0, sum)
        if self.sub:
            return True
        else:
            return False
        
    def helper(self, root, temp, sum):
        if not root:
            return
        if not root.left and not root.right:
            if sum - temp == root.val:
                self.sub.append(temp)
            return
        temp += root.val
        self.helper(root.left, temp, sum)
        self.helper(root.right, temp, sum)
        
