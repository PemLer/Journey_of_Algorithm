class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        是2的幂次方并且与3的余数是1
        """
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1
