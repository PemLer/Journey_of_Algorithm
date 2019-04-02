# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        self.helper(0,root,res)
        if len(res) > 1:
            for i in range(1,len(res),2):
                res[i] = res[i][::-1]
        return res
    
    def helper(self,i,root,res):
        if root:
            if len(res) == i: res.append([])
            res[i].append(root.val)
            self.helper(i+1,root.left,res)
            self.helper(i+1,root.right,res)
        
