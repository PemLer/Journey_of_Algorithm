class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.quick_pow(res, 10, 1337) * self.quick_pow(a, i, 1337)
        return res % 1337

    def quick_pow(self, x, n, m):
        res = 1
        while n > 0:
            if n & 1 == 1:
                res = res * x % m
            x = x * x % m
            n >>= 1
        return res
