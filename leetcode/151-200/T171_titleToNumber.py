class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {0:1,1:26,2:26**2,3:26**3,4:26**4,5:26**5,6:26**6,7:26**7,8:26**8,9:26**9,10:26**10}
        L = len(s)
        res = 0
        for i in range(0,L):
            res += (ord(s[i])-64)*d[L-1-i]
        return res

