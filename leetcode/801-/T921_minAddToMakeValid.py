class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        return len(stack)
