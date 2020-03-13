class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.res = self.tree_to_list()
        self.index = 0

    def tree_to_list(self):
        cur = self.root
        stack, res = [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur)
                cur = cur.right
        return res

    def next(self) -> int:
        """
        @return the next smallest number
        """
        value = self.res[self.index]
        self.index += 1
        return value.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.res)
