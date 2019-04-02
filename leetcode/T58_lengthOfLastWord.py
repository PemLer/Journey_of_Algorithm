class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()
        #print(s)
        L = len(s)
       # print(L)
        i = L - 1
        if ' ' not in s:
            return L
        else:
            while i > -1:
                if s[i] == ' ':
                    return L-i-1
                else:
                    i -= 1
            return 0

