# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.helper(root, [], 0, sum)
        return self.res

    def helper(self, root, tmp, sum, target):
        if not root:
            return
        sum += root.val
        if not root.left and not root.right:
            if sum == target:
                self.res.append(tmp+[root.val])
            return
        self.helper(root.left, tmp+[root.val], sum, target)
        self.helper(root.right, tmp+[root.val], sum, target)
