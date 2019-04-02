class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aa = int(a,2)
        bb = int(b,2)
        cc = aa+bb
        if cc == 0:
            return '0'
        else:
            c = str(bin(cc))
            c = c.lstrip('0b')

            return c

