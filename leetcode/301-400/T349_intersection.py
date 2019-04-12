class Solution:
    def intersection(self, nums1, nums2):
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
        d1={}
        for j in nums2:
            if (j in d) and (j not in d1):
                d1[j] = 1
                res.append(j)
        return res

