class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            count = k
            while stack and stack[-1][0] == c and stack[-1][1] == count - 1:
                stack.pop()
                count -= 1
            if count == k:
                if stack and stack[-1][0] == c:
                    stack.append([c, stack[-1][1]+1])
                else:
                    stack.append([c, 1])
        return ''.join([x[0] for x in stack])


if __name__ == '__main__':
    sol = Solution()
    ss = [
        ["deeedbbcccbdaa", 3],
        ["abcd", 2],
        ["pbbcggttciiippooaais", 2]
    ]
    for s in ss:
        print(sol.removeDuplicates(*s))
