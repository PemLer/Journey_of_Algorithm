class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n = 0
        if dividend < 0:
            dividend = -dividend
            n += 1
        if divisor < 0:
            divisor = -divisor
            n += 1

        if dividend == 0:
            res = 0
        elif dividend == divisor:
            res = 1
        elif dividend < divisor:
            res = 0
        elif divisor == 1:
            res = dividend
        else:
            t = 0
            b = divisor
            while b <= dividend:
                b = b << 1
                t += 1
            b = b >> 1
            t -+ 1
            res = 2**(t-1)

            t1 = []
            temp = dividend-b
            while temp>divisor:
                b = b >> 1
                if b <= temp:
                    temp -= b
                    t1.append(1)
                else:
                    t1.append(0)
                    continue
            for ii in range(0,len(t1)):
                if t1[ii] == 1:
                    res += 2**(t-ii-2)
        if n%2 == 1:
            res = -res
        else:
            res = res
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res

