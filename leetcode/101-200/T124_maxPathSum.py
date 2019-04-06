# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float('-inf')
        self.helper(root)
        return self.result
    
    """
    最大路径和：根据当前节点的角色，路径和可分为两种情况：
    一：以当前节点为根节点
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    4.当前节点+左右子树    
    这四种情况的最大值即为以当前节点为根的最大路径和
    此最大值要和已经保存的最大值比较，得到整个树的最大路径值
    
    二：当前节点作为父节点的一个子节点
    和父节点连接的话则需取【单端的最大值】
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    这三种情况的最大值    
    """
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        value1 = root.val
        value2 = value1 + left
        value3 = value1 + right
        value4 = value2 + right
        # 以此节点为根节点的最大值
        tmp = max(value1, value2, value3, value4)
        # 当前遍历树的最大值
        self.result = max(self.result, tmp)
        # 要和父节点关联，则需要取去除情况4的最大值
        return max(value1, value2, value3)
        
