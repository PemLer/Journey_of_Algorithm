class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        tmp = n
        while True:
            if tmp == 1:
                return True
            tmp = n >> 1
            if tmp == n/2:
                n = n//2
            else:
                return False
