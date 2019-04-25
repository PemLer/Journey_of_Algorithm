# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False
        l, r = len(array[0])-1, 0
        while l >= 0 and r < len(array):
            if array[r][l] < target:
                r += 1
            elif array[r][l] > target:
                l -= 1
            else:
                return True
        return False
