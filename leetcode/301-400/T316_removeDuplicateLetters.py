class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] in stack:
                continue
            while stack and ord(s[i]) < ord(stack[-1]) and s.find(stack[-1], i) != -1:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)
