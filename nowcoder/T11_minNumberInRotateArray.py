# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        l, r = 0, len(rotateArray)-1
        while l < r:
            mid = l + r >> 1
            if rotateArray[mid] >= rotateArray[0]:
                l = mid + 1
            else:
                r = mid
        return rotateArray[l]
