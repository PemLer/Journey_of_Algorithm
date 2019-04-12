class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return n
        count = 0
        for i in range(0,n):
            count =self.dec(s,i,i,count)
            count = self.dec(s,i,i+1,count)
        return count

    def dec(self,s,left,right,count):
        while left>=0 and right<len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

