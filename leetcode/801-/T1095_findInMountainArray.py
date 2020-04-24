# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        top = self.find_top(mountain_arr, n)

        l, r = 0, top
        while l <= r:
            mid = l + r >> 1
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = top + 1, n - 1
        while l <= r:
            mid = l + r >> 1
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

    def find_top(self, mountain_arr, n):
        l, r = 0, n - 1
        while l < r:
            mid = l + r >> 1
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        return l
