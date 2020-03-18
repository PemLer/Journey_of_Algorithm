class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        5 101
        6 110
        7 111
        两个相邻的数最低位与一定为0
        """
        zeros = 0
        while m < n:
            zeros += 1
            m >>= 1
            n >>= 1
        return m << zeros
