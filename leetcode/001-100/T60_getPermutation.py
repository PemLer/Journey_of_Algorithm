import time
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        n = 4， 参与排列的数字「1， 2， 3， 4」
        所有的排列
        1 + (permutations of 2, 3, 4)
        2 + (permutations of 1, 3, 4)
        3 + (permutations of 1, 2, 4)
        4 + (permutations of 1, 2, 3)
        n个数字的排列数为n!,那么3个数的排列数为6。假如k=14，那么第14个排列落在
        3 + (permutations of 1, 2, 4)
        令k=14-1(减去1是因为程序中索引从0开始), k/(n-1)!= 13/(4-1)! = 2, 在数列「1， 2， 3， 4」中索引为2的数字为3，所以第一个数字为3。
        那么问题进一步缩小为「1， 2， 4」数字的排列，求第 k= k%(n-1)!=13%(4-1)=1 个排列：
        1 + (permutations of 2, 4)
        2 + (permutations of 1, 4)
        4 + (permutations of 1, 2)
        在这一步中，2个数字排列有2!， 总共有3*2!=6个，我们寻找第一个排列，那么落在
        1 + (permutations of 2, 4)
        """
        nums = [x for x in range(1, n+1)]

        k -= 1
        res = []
        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res.append(nums.pop(a))

        return ''.join(map(str, res))


if __name__ == '__main__':
    sol = Solution()
    start_time = time.time()
    print(sol.getPermutation(9, 353955))
    print('cost:', time.time() - start_time)
