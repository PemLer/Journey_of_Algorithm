from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        def cal(k):
            res = 0
            for a in arr:
                res += min(a, k)
            return res

        n = len(arr)
        l, r = 0, 10_000
        while l < r:
            mid = l + (r - l) // 2
            if cal(mid) < target:
                l = mid + 1
            else:
                r = mid

        if l > 0 and abs(cal(l - 1) - target) <= abs(cal(l) - target):
            return l - 1
        else:
            return l


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 9, 3]
    target = 10
    print(sol.findBestValue(nums, target))
