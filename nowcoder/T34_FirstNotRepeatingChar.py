# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        s_dic = dict()
        res = ''
        for i in s[::-1]:
            if i not in s_dic:
                res = i
                s_dic[i] = 1
            else:
                s_dic[i] += 1
        return res

if __name__ == '__main__':
    s = 'google'
    sol = Solution()
    print(sol.FirstNotRepeatingChar(s))