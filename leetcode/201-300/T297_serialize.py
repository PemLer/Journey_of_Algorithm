# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.seria(root, res)
        return ','.join(res)

    def seria(self, root, res):
        if not root:
            res.append('None')
            return
        res.append(str(root.val))
        self.seria(root.left, res)
        self.seria(root.right, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')
        if len(res) == 0:
            return
        v = res.pop(0)
        if v != 'None':
            root = TreeNode(int(v))
            root.left = self.deseria(res)
            root.right = self.deseria(res)
            return root
        else:
            return None

    def deseria(self, res):
        if not res:
            return
        v = res.pop(0)
        if v != 'None':
            node = TreeNode(int(v))
            node.left = self.deseria(res)
            node.right = self.deseria(res)
            return node
        else:
            return None
