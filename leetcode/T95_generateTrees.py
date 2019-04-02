# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1,n)
        
    def dfs(self,a,b):
        if a > b:
            return [None]
        res = []
        for val in range(a,b+1):
            left = self.dfs(a,val-1)
            right = self.dfs(val+1,b)
            for i in left:
                for j in right:
                    root = TreeNode(val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
