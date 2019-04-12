# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.dic = set()
        return self.helper(root, k)
    
    def helper(self, root, k):
        if not root:
            return False
        l = self.helper(root.left, k)
        if k - root.val in self.dic:
            return True
        else:
            self.dic.add(root.val)
        r = self.helper(root.right, k)
        return l or r
