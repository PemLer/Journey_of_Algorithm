class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
        s = s.lower()
        res = ''
        for i in s:
            if i in d:
                res += i
                
        if res == res[::-1]:
            return True
        return False
        
        
    
        
