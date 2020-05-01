class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1 + nums2
        res.sort()
        n = len(res) // 2
        return res[n] if len(res) % 2 == 1 else (res[n] + res[n - 1]) / 2


# 二分
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 为了搜索长度更短的那个
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        left_total = m + n + 1 >> 1
        while left < right:
            i = left + right >> 1
            j = left_total - i

            if nums2[j - 1] > nums1[i]:
                left = i + 1
            else:
                right = i

        i = left
        j = left_total - left

        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]

        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        if (m + n) & 1:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2