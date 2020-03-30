# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # 归并排序的变化版本
        self.count = 0
        self.merge_sort(data)
        return self.count % 1000000007

    def merge_sort(self, data):
        length = len(data)
        if length < 2:
            return data
        mid = length // 2
        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])
        return self.merge_and_count(left, right)

    def merge_and_count(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                self.count += len(left[i:])
        res.extend(left[i:])
        res.extend(right[j:])
        return res


if __name__ == '__main__':
    sol = Solution()
    data = [1,2,3,4,5,6,7,0]
    print(sol.InversePairs(data))