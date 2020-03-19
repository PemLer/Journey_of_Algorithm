class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        for _ in range(32):
            if mask > num:
                break
            num ^= mask
            mask <<= 1
        return num
