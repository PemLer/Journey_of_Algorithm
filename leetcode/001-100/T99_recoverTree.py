# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []
        self.mid_travel(root)
        lst = []
        for i in range(1, len(self.res)):
            if self.res[i].val < self.res[i-1].val:
                lst.append(i)
        if len(lst) == 1:
            self.res[lst[0]].val, self.res[lst[0]-1].val = self.res[lst[0]-1].val, self.res[lst[0]].val
        elif len(lst) == 2:
            self.res[lst[0]-1].val, self.res[lst[1]].val = self.res[lst[1]].val, self.res[lst[0]-1].val
                
        
    def mid_travel(self, root):
        if not root:
            return 
        self.mid_travel(root.left)
        self.res.append(root)
        self.mid_travel(root.right)
        
