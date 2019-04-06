class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = len(str(n))
        if n / (10 ** (l-1)) == 0:
            return True
        d = {n: 1}
        while 1:
            i = 0
            l = len(str(n))
            for j in range(l - 1, -1, -1):
                i += (n // (10 ** j))**2
                n -= (n // (10 ** j)) * (10 ** j)
                #print(i)
            if i / (10 ** (len(str(i))-1)) == 1:
                return True
            if i == 1:
                return True
            if i in d:
                return False
            if i not in d:
                d[i] = 1
                n = i


