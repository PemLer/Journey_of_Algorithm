from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        cur = 0
        for s in pushed:
            stack.append(s)
            while stack and stack[-1] == popped[cur]:
                stack.pop()
                cur += 1
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 2, 4, 5]
    print(sol.validateStackSequences(pushed, popped))
