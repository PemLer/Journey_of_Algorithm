class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        cur = 0
        for char in t:
            if char == s[cur]:
                cur += 1
            if cur == len(s):
                return True
        return False
