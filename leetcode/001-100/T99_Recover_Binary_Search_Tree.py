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
        1 中序遍历
        2 寻找被交换的两个节点 
        3 恢复
        """
        def inorder_travel(root):
            return inorder_travel(root.left) + [root.val] + inorder_travel(root.right) if root else []
        
        def find_two_elements(numbers):
            x, y = -1, -1
            for i in range(len(numbers) - 1):
                if numbers[i+1] < numbers[i]:
                    y = numbers[i+1]
                    # 找到第一个
                    if x == -1:
                        x = numbers[i]
                    # 找到第二个
                    else:
                        break
            return x, y
        
        def recover(root, count):
            if root:
                if root.val == x or root.val == y:
                    root.val = x if root.val == y else y
                    count -= 1
                    if count == 0:
                        return 
                recover(root.left, count)
                recover(root.right, count)
                
        numbers = inorder_travel(root)
        x, y = find_two_elements(numbers)
        recover(root, 2)
