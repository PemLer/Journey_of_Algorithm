class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        d = {}
        t = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                d[t] = nums1[i]
                i += 1
                t += 1
            elif nums1[i] > nums2[j]:
                d[t] = nums2[j]
                j += 1
                t += 1
            elif nums1[i] == nums2[j]:
                d[t] = nums1[i]
                d[t+1] = nums2[j]
                t += 2
                i += 1
                j += 1

        if i < m:
            for k in range(i,m):
                d[t] = nums1[k]
                t += 1
        if j < n:
            for kk in range(j,n):
                d[t] = nums2[kk]
                t += 1
        for ii in range(0,t):
            nums1[ii] = d[ii]

