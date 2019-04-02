# # -*- coding:utf-8 -*-
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         dp = [array[0]]
#         for i in range(1, len(array)):
#             if dp[i-1] <= 0:
#                 dp.append(array[i])
#             else:
#                 dp.append(dp[i-1]+array[i])
#         return max(dp)

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        length = len(array)
        maxl = 0
        res = float('-inf')
        for i in range(length):
            if maxl < 0:
                maxl = 0
            maxl += array[i]
            res = max(res, maxl)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))