# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack_ass = []
        i = 0
        while pushV and popV and i < len(pushV):
            if pushV[i] == popV[0]:
                stack_ass.append(pushV.pop(i))
                popV.pop(0)
                i -= 1
            else:
                i += 1

        if popV:
            return False
        else:
            return True

sol = Solution()
pushv = [1,2,3,4,5]
popv = [4,5,3,2,1]
print(sol.IsPopOrder(pushv, popv))
