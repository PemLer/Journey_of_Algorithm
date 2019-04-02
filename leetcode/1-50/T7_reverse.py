class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x1 = str(x)
            x2 = x1[::-1]
            x3 = x2.replace('-', '')
            x4 = -int(x3)
            if x4 < -2**31:
                return 0
            else:
                return x4
        else:
            x1 = str(x)
            x2 = x1[::-1]
            x4 = int(x2)
            if x4 > 2**31-1:
                return 0
            else:
                return x4
