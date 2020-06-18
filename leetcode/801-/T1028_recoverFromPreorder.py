class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        """
        "1-2--3--4-5--6--7"
        "1-2--3---4-5--6---7"
        "1-401--349---90--88"
        """
        nodes = []
        i = 0
        while i < len(S):
            count = 0
            while i < len(S) and S[i] == '-':
                i += 1
                count += 1
            val = 0
            while i < len(S) and S[i] != '-':
                val = val * 10 + int(S[i])
                i += 1
            nodes.append((val, count))

        stack = []
        root = TreeNode(nodes[0][0])
        stack.append((root, 0))
        for i in range(1, len(nodes)):
            val, layer = nodes[i]
            new_node = TreeNode(val)
            while stack and stack[-1][1] + 1 != layer:
                stack.pop()
            if stack:
                par = stack[-1][0]
                if par.left:
                    par.right = new_node
                else:
                    par.left = new_node
                stack.append((new_node, layer))
        return root