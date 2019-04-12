class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        List1 = [0]
        while len(List1) <= num:
            List2 = [x+1 for x in List1]
            List1 += List2
        return List1[:num+1]

