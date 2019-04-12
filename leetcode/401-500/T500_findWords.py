class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = 'qwertyuiop'
        s2 = 'asdfghjkl'
        s3 = 'zxcvbnm'
        t = 0
        res = []
        for s in words:
            ss = s.lower()
            sign = 1
            for i in range(0, len(s)):
                if i == 0 and ss[0] in s1:
                    t = 1
                elif i == 0 and ss[0] in s2:
                    t = 2
                elif i == 0 and ss[0] in s3:
                    t = 3

                if t == 1 and ss[i] not in s1:
                    sign = 0
                    break
                if t == 2 and ss[i] not in s2:
                    sign = 0
                    break
                if t == 3 and ss[i] not in s3:
                    sign = 0
                    break
            if sign == 1:
                res.append(s)
        return res

