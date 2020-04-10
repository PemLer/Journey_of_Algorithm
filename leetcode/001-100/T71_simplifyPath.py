class Solution:
    def simplifyPath(self, path: str) -> str:
        t = ''
        items = []
        for p in path:
            if p != '/':
                t += p
            else:
                if t:
                    items.append(t)
                t = ''
        if t:
            items.append(t)

        stack = []
        for item in items:
            if item == '..':
                if stack:
                    stack.pop()
            elif item == '.':
                continue
            else:
                stack.append(item)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    sol = Solution()
    paths = [
        "/home/",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/",
        "/a/../../b/../c//.//",
        "/a//b////c/d//././/.."
    ]
    for path in paths:
        print(sol.simplifyPath(path))
