class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        d = {}
        for i in range(0,int(c**0.5)+1):
            d[i * i] = 1
            if c - i*i in d:
                return True
            else:
                d[i*i] = 1
        return False
