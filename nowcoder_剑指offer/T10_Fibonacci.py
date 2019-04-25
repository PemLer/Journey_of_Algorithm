# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        a, b = 1, 1
        res = 0
        for i in range(3, n+1):
            res = a + b
            a, b = b, res
        return res
