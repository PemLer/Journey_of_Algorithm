class Solution:
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        a, b = 1, 1
        mod = 1000000007
        for i in range(2, n+1):
            a, b = b, a + b
        return b % mod