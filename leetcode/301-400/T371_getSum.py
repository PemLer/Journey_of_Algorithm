class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        异或得到不进位相加，和得到需进位的前一位
        重复进行，知道需要进位的数为0
        """
        MASK = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
