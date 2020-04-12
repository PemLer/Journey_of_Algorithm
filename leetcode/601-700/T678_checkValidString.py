class Solution:
    def checkValidString(self, s: str) -> bool:
        le, ri = 0, 0
        for c in s:
            if c == '(':
                le += 1
                ri += 1
            elif c == '*':
                if le > 0:
                    le -= 1
                ri += 1
            else:
                if le > 0:
                    le -= 1
                ri -= 1
            if ri < 0:
                return False
        return le == 0