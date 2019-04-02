# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # 双指针
        res = []
        left = 1
        right = 2
        end = (tsum+1) // 2
        while left < right and right <= end:
            # print(left, right)
            tol = (left + right) * (right - left + 1) / 2
            if tol == tsum:
                res.append([x for x in range(left, right+1)])
                left += 1
            elif tol < tsum:
                right += 1
            elif tol > tsum:
                left += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.FindContinuousSequence(100))
    print(sol.FindContinuousSequence(3))