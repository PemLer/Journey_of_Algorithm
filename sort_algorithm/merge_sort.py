# -*- coding=utf-8 -*-
# 归并排序算法
import random


class Solution():
    def merge_sort(self, lst):
        n = len(lst)
        tmp = [0] * n
        nums = self.merge(lst, tmp, 0, n - 1)
        return nums

    def merge(self, lst, tmp, left, right):
        if left >= right:
            return
        mid = left + right >> 1
        self.merge(lst, tmp, left, mid)
        self.merge(lst, tmp, mid + 1, right)
        i, j, pos = left, mid + 1, left
        while i <= mid and j <= right:
            if lst[i] < lst[j]:
                tmp[pos] = lst[i]
                i += 1
            else:
                tmp[pos] = lst[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = lst[k]
            pos += 1
        for k in range(j, right + 1):
            tmp[pos] = lst[k]
            pos += 1
        lst[left:right + 1] = tmp[left:right + 1]
        return lst


if __name__ == '__main__':
    x = [i for i in range(100)]
    random.shuffle(x)
    sol = Solution()
    print(sol.merge_sort(x))
