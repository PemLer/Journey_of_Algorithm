class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def helper(S):
            stack1 = []
            for s in S:
                if s == '#':
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(s)
            return stack1

        return helper(S) == helper(T)