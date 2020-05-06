class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        1-9 10-99 100-999
        9*1 90*2  900*3
        1 确定是几位数
        2 确定是第几个数
        3 确定是第几位
        """
        base, digit = 9, 1
        while n - base * digit > 0:
            n -= base * digit
            digit += 1
            base *= 10

        a, b = divmod(n - 1, digit)
        return int(str(10 ** (digit - 1) + a)[b])

