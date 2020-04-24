from typing import List


# 方法一 双指针
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n == k:
            return arr
        l, r = 0, n - 1
        while l < r:
            left = abs(arr[l] - x)
            right = abs(arr[r] - x)
            if left > right:
                l += 1
            elif left < right:
                r -= 1
            else:
                r -= 1
            if r - l + 1 == k:
                return [x for x in arr[l:r+1]]


# 方法二 二分
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        二分寻找区间的左边界
        """
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l + k]
