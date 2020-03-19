class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        for ch in s:
            a ^= ord(ch)

        for ch in t:
            a ^= ord(ch)
        return chr(a)
