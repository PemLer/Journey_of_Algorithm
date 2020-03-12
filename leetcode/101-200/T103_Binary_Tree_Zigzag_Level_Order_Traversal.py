# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        self.helper(root, 0, levels)
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i] = levels[i][::-1]
        return levels

    def helper(self, root, level, levels):
        """
        layer记录层数
        """
        if not root:
            return
        if level == len(levels):
            levels.append([])
        levels[level].append(root.val)
        self.helper(root.left, level+1, levels)
        self.helper(root.right, level+1, levels)
