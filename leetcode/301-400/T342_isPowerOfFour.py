class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num == 0:
            return False
        else:
            if num/4 != int(num/4):
                return False
            else:
                return self.isPowerOfFour(int(num/4))
        
