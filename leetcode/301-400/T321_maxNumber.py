from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def pick(nums, k):
            if not k:
                return []
            res, _pop = [], len(nums) - k
            while nums:
                num = nums.pop(0)
                while _pop and res and res[-1] < num:
                    _pop -= 1
                    res.pop()
                res.append(num)
            return res[:k]

        def merge(nums1, nums2):
            res = []
            while nums1 and nums2:
                res.append(nums1.pop(0)) if nums1 > nums2 else res.append(nums2.pop(0))
            res.extend(nums1 or nums2)
            return res

        l1, l2 = len(nums1), len(nums2)
        ans = []
        for i in range(k+1):
            c1, c2 = i, k-i
            if c1 > l1 or c2 > l2:
                continue
            res1 = pick(nums1.copy(), c1)
            res2 = pick(nums2.copy(), c2)

            res = merge(res1, res2)

            if res > ans:
                ans = res
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(sol.maxNumber(nums1, nums2, k))
