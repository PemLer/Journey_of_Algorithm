# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        v = pre.pop(0)
        node = TreeNode(v)
        index = tin.index(v)
        node.left = self.reConstructBinaryTree(pre, tin[:index])
        node.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return node
