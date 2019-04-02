# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        def compare(num1, num2):
            if str(num1) + str(num2) > str(num2) + str(num1):
                return num2, num1
            else:
                return num1, num2

        for num in range(len(numbers)):
            for i in range(1, len(numbers)):
                numbers[i-1], numbers[i] = compare(numbers[i-1], numbers[i])
        return ''.join([str(x) for x in numbers])

if __name__ == '__main__':
    sol = Solution()
    numbers = [3,32,321]
    print(sol.PrintMinNumber(numbers))
