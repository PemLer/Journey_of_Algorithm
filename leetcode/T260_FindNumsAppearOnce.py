# -*- coding:utf-8 -*-
# 解法一
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        num_dict = dict()
        for num in array:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
                 
        res = []
        for key, val in num_dict.items():
            if val == 1:
                res.append(key)
        return res

# -*- coding:utf-8 -*-
# 解法二
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        tmp = 0
        # 对array中数进行异或
        for i in array:
            tmp ^= i
        # 找到tmp中最低位为1的index
        index = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            index += 1
        # 两组数分别异或
        a = b = 0
        for i in array:
            if self.isBit(i, index):
                a ^= i
            else:
                b ^= i
        return [a, b]
                 
    def isBit(self, num, index):
        num >>= index
        return num & 1

