class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        d = ['-','+']
        str = str.lstrip()
        L = len(str)
        res = ''
        for i in str:
            if i in d and len(res)==0:
                res += i
            elif ord(i)>=48 and ord(i)<=57:
                res += i
            else:
                break
        if len(res)==0:
            return 0
        elif len(res)==1 and res[0] in d:
            return 0
        else:
            val = int(res)
            if val < -2**31:
                return int(-2**31)
            elif val > 2**31-1:
                return int(2**31-1)
            else:
                return val
        

