class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # 计算无效的括号
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        # 获取答案
        res = []
        for i in range(len(s)):
            if i not in stack:
                res.append(s[i])

        return ''.join(res)


