class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #print(s)
        table = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        a = len(s)
        d = 0
        i = 0
        while i < a:
        #for i in range(0,a):
            if i != a-1 and table[s[i]] < table[s[i+1]]:
                d = d+(table[s[i+1]]-table[s[i]])
                i += 2
            else:
                d = d+table[s[i]]
                i += 1
        return d
