class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        index = 1
        while index < n:
            val = min(res[index2]*2, res[index3]*3, res[index5]*5)
            if val == res[index2]*2:
                index2 += 1
                if val in res:
                    continue
            elif res[index3]*3 == val:
                index3 += 1
                if val in res:
                    continue
            elif res[index5]*5 == val:
                index5 += 1
                if val in res:
                    continue
            res.append(val)
            index += 1
        return res[-1]
