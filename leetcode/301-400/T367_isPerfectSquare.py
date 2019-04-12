class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num
        while low <= high:
            mid = int((low+high)/2)
            if mid**2 == num:
                return True
            elif mid**2 > num:
                high = mid-1
            elif mid**2 < num:
                low = mid+1
        return False
