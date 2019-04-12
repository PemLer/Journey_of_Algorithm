class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {'a':0,'A':0,'e':0,'E':0,'i':0,'I':0,'o':0,'O':0,'u':0,'U':0}
        s1 = ''
        s = list(s)
        for i in s:
            if i in d:
                s1 += i
        s2 = s1[::-1]
        
        t = 0
        # s3 = s
        for i in range(0,len(s)):
            if s[i] in d:
                s[i] = s2[t]
                t += 1
                
        return ''.join(s)
        
