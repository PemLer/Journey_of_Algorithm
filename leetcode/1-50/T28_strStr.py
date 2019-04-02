class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        L1 = len(haystack)
        L2 = len(needle)
        if L2 != 0:
            for i in range(0,L1):
                if haystack[i] == needle[0] and i+L2-1 < L1:
                    if haystack[i:i+L2] == needle:
                        return i
            return -1
        else:
            return 0

