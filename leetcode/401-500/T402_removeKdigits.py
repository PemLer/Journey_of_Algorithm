class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)

        stack = stack[:-k] if k else stack

        return ''.join(stack).lstrip('0') or '0'
