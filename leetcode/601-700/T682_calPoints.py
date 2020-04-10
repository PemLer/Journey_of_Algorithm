from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        total = 0
        for op in ops:
            if op == 'C':
                value = stack.pop()
                total -= value
            elif op == 'D':
                value = stack[-1] * 2
                stack.append(value)
                total += value
            elif op == '+':
                value = stack[-1] + stack[-2]
                stack.append(value)
                total += value
            else:
                value = int(op)
                stack.append(value)
                total += value

        return total