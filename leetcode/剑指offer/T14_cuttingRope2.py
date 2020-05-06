class Solution:
    def cuttingRope(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n == 2:
            return 1
        elif n == 3:
            return 2

        @lru_cache(None)
        def dp(k):
            if k > 4:
                return dp(k - 3) * 3 % mod
            elif k == 4:
                return 4
            elif k == 3:
                return 3
            elif k == 2:
                return 2

        return dp(n) % mod