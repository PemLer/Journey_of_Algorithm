from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2 / v1))
            elif token == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif token == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 + v1)
            elif token == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 * v1)
            else:
                stack.append(int(token))
        return stack[-1]


if __name__ == '__main__':
    nums = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ]
    sol = Solution()
    for num in nums:
        print(sol.evalRPN(num))
