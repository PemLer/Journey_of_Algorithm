# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        sub = str(root.val)
        self.res = []
        self.dfs(root,sub)
        return self.res
        
    def dfs(self,root,sub):
        if not root.left and not root.right:
            self.res.append(sub)
        elif root.left and root.right:
            self.dfs(root.left,sub+'->'+str(root.left.val))
            self.dfs(root.right,sub+'->'+str(root.right.val))
        elif root.left:
            self.dfs(root.left,sub+'->'+str(root.left.val))
        else:
            self.dfs(root.right,sub+'->'+str(root.right.val))
