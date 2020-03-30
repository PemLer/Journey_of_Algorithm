# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        s = s.strip()
        tag = True
        if s.startswith('+'):
            tag = True
            s = s[1:]
        elif s.startswith('-'):
            tag = False
            s = s[1:]
        res = 0
        for i in s:
            try:
                res = res * 10 + int(i)
            except:
                return 0
        if not tag:
            return -res
        else:
            return res


# # -*- coding:utf-8 -*-
# class Solution:
#     def StrToInt(self, s):
#         # write code here
#         numlist=['0','1','2','3','4','5','6','7','8','9','+','-']
#         sum=0
#         label=1#正负数标记
#         if s=='':
#             return 0
#         for string in s:
#             if string in numlist:#如果是合法字符
#                 if string=='+':
#                     label=1
#                     continue
#                 if string=='-':
#                     label=-1
#                     continue
#                 else:
#                     sum=sum*10+numlist.index(string)
#             if string not in numlist:#非合法字符
#                 sum=0
#                 break#跳出循环
#         return sum*label


if __name__ == '__main__':
    sol = Solution()
    print(sol.StrToInt('+2147483647'))
    print(sol.StrToInt('2147483647'))