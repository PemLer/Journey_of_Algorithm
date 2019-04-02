class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        d1 = {'.': 0, 'e': 0}
        d2 = {'-': 0, '+': 0}
        d3 = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '.': 0, 'e': 0, '-': 0,
              '+': 0}
        s = s.strip()
        t = 0
        if len(s) == 0:
            return False
        elif len(s) == 1 and s[0] not in d:
            return False

        for i in range(0, len(s)):
            if (s[i] == '-' or s[i] == '+') and i != 0 and s[i-1] != 'e':
                # print(1)
                return False

            if (s[i] == '-' or s[i] == '+') and len(s[i:]) == 1:
                return False

            if (s[i] == '-' or s[i] == '+') and len(s[i:]) > 1 and s[i + 1] == 'e':
                # print(1)
                return False

            if s[i] == '.' and d1['.'] != 0:
                # print(2)
                return False
            elif i == 0 and s[i] == '.' and len(s[i:]) > 1 and s[i + 1] == 'e':
                return False
            elif s[i] == '.':
                d1['.'] += 1

            if s[i] == 'e' and (i == 0 or i == len(s) - 1 or d1['e'] != 0):
                # print(3)
                return False
            elif s[i] == 'e':
                for j in s[i + 1:]:
                    if j == '.':
                        return False
                d1['e'] += 1

            if s[i] not in d3:
                # print(5)
                return False
            if s[i] in d:
                t += 1

        if t != 0:
            return True
        else:
            return False
