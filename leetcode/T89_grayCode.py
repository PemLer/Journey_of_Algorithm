class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n > 1:
            temp1 = self.grayCode(n-1)
            temp2 = temp1[::-1]
            temp3 = [x+2**(n-1) for x in temp2]
            return temp1 + temp3
