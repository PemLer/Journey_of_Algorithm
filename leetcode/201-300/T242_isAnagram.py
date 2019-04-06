class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        L1 = len(s)
        L2 = len(t)
        if L1 != L2:
            return False
        else:
            d = {}
            for i in s:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

            for j in t:
                if j not in d:
                    return False
                else:
                    d[j] -= 1
                    if d[j] < 0:
                        return False
            return True

