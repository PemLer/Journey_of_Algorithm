# -*- coding:utf-8 -*-
# 冒泡排序
class Solution():
    def bubble_sort_v2(self, lst):
        for _ in range(len(lst)):
            tag = False
            for i in range(1, len(lst)):
                if lst[i-1] > lst[i]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
                    tag = True
            if not tag:
                break
        # return lst

if __name__ == '__main__':
    import random
    sol = Solution()
    lst = [x for x in range(1, 100)]
    random.shuffle(lst)
    sol.bubble_sort_v2(lst)
    print(lst)
