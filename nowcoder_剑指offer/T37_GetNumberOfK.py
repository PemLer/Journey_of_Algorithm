# # -*- coding:utf-8 -*-
# class Solution:
#     def GetNumberOfK(self, data, k):
#         index = self.binary_search(data, k)
#         if not index:
#             return None
#         count = 1
#         if index > 0:
#             for i in range(index - 1, 0, -1):
#                 if data[i] != k:
#                     break
#                 else:
#                     count += 1
#         if index < len(data) - 1:
#             for i in range(index + 1, len(data)):
#                 if data[i] != k:
#                     break
#                 else:
#                     count += 1
#         return count
#
#     def binary_search(self, data, k):
#         if not data:
#             return None
#         length = len(data)
#         left = 0
#         right = length - 1
#         while left < right:
#             mid = (left + right) // 2
#             if data[mid] == k:
#                 return mid
#             elif data[mid] < k:
#                 left = mid
#             else:
#                 right = mid
#         return None

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        l = 0
        r = len(data) - 1
        first = self.binary_search_first(data, k, l, r)
        end = self.binary_search_end(data, k, l, r)
        return end - first + 1

    def binary_search_first(self, data, k, l, r):
        while l <= r:
            mid = (l + r) // 2
            if data[mid] == k and (mid == 0 or data[mid - 1] != k):
                return mid
            if data[mid] < k:
                l = mid+1
            else:
                r = mid-1
        return -1

    def binary_search_end(self, data, k, l, r):
        while l <= r:
            mid = (l + r) // 2
            if data[mid] == k and (mid == len(data) - 1 or data[mid + 1] != k):
                return mid
            if data[mid] <= k:
                l = mid+1
            else:
                r = mid-1
        return -2

if __name__ == '__main__':
    sol = Solution()
    data = [1,3,3,3,3,4,5]
    k = 2
    print(sol.GetNumberOfK(data, k))