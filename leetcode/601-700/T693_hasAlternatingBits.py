class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mask = 0
        flag = n % 2
        ans = True
        while (1 << mask) <= n:
            bit = n >> mask & 1
            if bit != flag:
                ans = False
                break
            flag = (flag + 1) % 2
            mask += 1
        return ans
