class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = True
        if n < 0:
            sign = False
            n = -n

        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        if not sign:
            ans = 1 / ans
        return ans