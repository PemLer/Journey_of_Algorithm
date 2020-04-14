class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                tmp = ''
                while stack and stack[-1] != '(':
                    tmp = stack.pop() + tmp
                stack.pop()
                stack.append(tmp[::-1])
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    ss = [
        '(u(love)i)',
        "(abcd)",
        "(ed(et(oc))el)",
        "a(bcdefghijkl(mno)p)q"
    ]
    for s in ss:
        print(sol.reverseParentheses(s))
