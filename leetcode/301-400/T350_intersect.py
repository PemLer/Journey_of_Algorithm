class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L1 = len(nums1)
        L2 = len(nums2)
        d={}
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        res = []
        for j in nums2:
            if j in d and d[j] != 0:
                res.append(j)
                d[j] -= 1
        return res

