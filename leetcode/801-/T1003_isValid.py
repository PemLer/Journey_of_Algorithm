class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for s in S:
            if s == 'c' and len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                stack.pop()
                stack.pop()
            else:
                stack.append(s)

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    ss = [
        "aabcbc",
        "abcabcababcc",
        "abccba",
        "cababc",
    ]
    for s in ss:
        print(sol.isValid(s))
