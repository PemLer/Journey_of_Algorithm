class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {')': '(', ']': '[', '}': '{'}
        l = [None]  # 设置None是为了排除空值的情况！
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l) == 1  # 用来排除空值的情况
