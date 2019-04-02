# -*- coding:utf-8 -*-
# 快速排序
import random
class Solution():
    def quick_sort_v2(self, lst):
        if not lst:
            return []
        piov = lst[0]
        left = [x for x in lst[1:] if x < piov]
        right = [x for x in lst[1:] if x > piov]
        return self.quick_sort_v2(left) + [piov] + self.quick_sort_v2(right)

if __name__=='__main__':
    sol = Solution()
    lst = []
    x = [i for i in range(1, 101)]
    for i in range(100):
        lst.append(random.choice(x))
    print(sol.quick_sort_v2(lst))
