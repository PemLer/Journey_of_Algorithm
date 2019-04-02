class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = len(strs)
        if a<1:
            return ""
        elif a == 1:
            return strs[0]
        else:
            b = len(strs[0])
            for i in range(1,a):
                b = min(b,len(strs[i]))
            d = 0
            for k in range(0,b):
                t = 0
                for j in range(1,a):
                    if strs[0][k] == strs[j][k]:
                        t += 1
                if t == a-1:
                    d += 1
                else:
                    break
            return strs[0][0:d]



