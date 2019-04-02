class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join(str(i) for i in digits)
        s = int(s)+1
        s = list(str(s))
        s = list(map(int,s))
        return s

