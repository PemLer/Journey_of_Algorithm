from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def is_eat_up(k):
            t = 0
            for pile in piles:
                if pile % k == 0:
                    t += pile // k
                else:
                    t += pile // k + 1
            return t <= H

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if not is_eat_up(mid):
                l = mid + 1
            else:
                r = mid

        return l


if __name__ == '__main__':
    piles = [30,11,23,4,20]
    H = 6
    sol = Solution()
    print(sol.minEatingSpeed(piles, H))
