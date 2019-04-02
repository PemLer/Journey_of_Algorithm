# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        sub = []
        self.helper(root, expectNumber, [], sub)
        return sub

    def helper(self, root, expectNumber, temp, sub):
        if not root:
            return
        if not root.left and not root.right:
            if root.val + sum(temp) == expectNumber:
                sub.append(temp+[root.val])
            return

        self.helper(root.left, expectNumber, temp+[root.val], sub)
        self.helper(root.right, expectNumber, temp+[root.val], sub)

if __name__ == '__main__':
    a = {10,5,12,4,7}
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(12)
    root.left = left
    root.right = right
    right1 = TreeNode(7)
    left1 = TreeNode(12)
    left.left = right1
    # right.right = left1

    sol = Solution()
    print(sol.FindPath(root, 22))