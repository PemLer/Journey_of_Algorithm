class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = []
        for s in S:
            if not stack:
                stack.append(s)
            else:
                if stack and len(stack) == 1 and s == ')':
                    stack.pop()
                elif s == '(':
                    stack.append(s)
                    res.append(s)
                elif s == ')':
                    stack.pop()
                    res.append(s)

        return ''.join(res)