class Solution:

    def isUnique(self, astr: str):
        mark = 0
        for s in astr:
            num = ord(s) - ord('a')
            if mark & (1 << num):
                return False
            mark |= (1 << num)
        return True
