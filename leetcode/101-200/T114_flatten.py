# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                # root左边的第一个节点
                pre = root.left

                # 寻找最右边的节点
                while pre.right:
                    pre = pre.right

                # 连上root的右边子树
                pre.right = root.right

                # root的左边转换到右边
                root.right = root.left
                root.left = None

                # 开始修改下一个节点
                root = root.right
