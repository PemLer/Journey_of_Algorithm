class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {0: 1}
        total = 0
        res = 0
        for num in A:
            total += num
            mod = total % K
            if mod in d:
                res += d[mod]
                d[mod] += 1
            else:
                d[mod] = 1
        return res