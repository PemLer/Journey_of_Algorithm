# -*- coding=utf-8 -*-
# 归并排序算法
import random
class Solution():
    def merge_sort(self, lst):
        if len(lst) < 2:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

if __name__ == '__main__':
    x = [i for i in range(100)]
    random.shuffle(x)
    sol = Solution()
    print(sol.merge_sort(x))
