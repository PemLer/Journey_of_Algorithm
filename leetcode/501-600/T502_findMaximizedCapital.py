from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        p_and_c = []
        for p, c in zip(Profits, Capital):
            p_and_c.append([p, c])
        p_and_c.sort(key=lambda x: -x[0])
        # print(p_and_c)

        ans = W
        for _ in range(k):
            i = 0
            while i < len(p_and_c):
                p, c = p_and_c[i]
                if W >= c:
                    ans += p
                    W += p
                    p_and_c.pop(i)
                    break
                i += 1

        return ans
