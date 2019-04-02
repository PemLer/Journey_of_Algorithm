# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.sub = []
        self.mid_travel(pRootOfTree)
        for i, v in enumerate(self.sub[:-1]):
            v.right = self.sub[i + 1]
            self.sub[i + 1].left = v
        return self.sub[0]

    def mid_travel(self, root):
        if not root:
            return
        self.mid_travel(root.left)
        self.sub.append(root)
        self.mid_travel(root.right)

if __name__=="__main__":
    sol = Solution()
    node1 = TreeNode(5)
    node2 = TreeNode(2)
    node3 = TreeNode(8)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node7 = TreeNode(9)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    root = sol.Convert(node1)
    while root:
        print(root.val)
        root = root.right
