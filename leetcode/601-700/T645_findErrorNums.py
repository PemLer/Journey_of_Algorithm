class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        temp1 = None
        m = 0
        for i in nums:
            if i not in d:
                d[i] = 1
                m = max(m,i)
            else:
                temp1 = i
        temp2 = 0
        for i in range(1,m):
            if i not in d:
                temp2 = i
                return [temp1,temp2]
        if 1 not in d:
            return [temp1,1]
        else:
            return [temp1,m+1]
