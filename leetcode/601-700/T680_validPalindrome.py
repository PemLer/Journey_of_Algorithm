class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        t = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                temp1 = s[:l] + s[l+1:]
                temp2 = s[:r] + s[r+1:]
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                    return True
                else:
                    return False
        return True
                
        
        
