class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = ''
        s = 1
        while s != 0:
            s = n//26
            y = n%26
            if y == 0 and s == 1:
                y = 26
                s = 0
            elif y == 0 and s != 1:
                y = 26
                s = s - 1
            str += chr(y+64)
            n = s
        str = str[::-1]
        return str

