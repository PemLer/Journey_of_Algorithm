class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = dict()
        for a in A:
            for b in B:
                if a + b not in dic:
                    dic[a+b] = 1
                else:
                    dic[a+b] += 1
        
        ans = 0
        for c in C:
            for d in D:
                if - (c + d) in dic:
                    ans += dic[-(c+d)]
        return ans
        
